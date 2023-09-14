#import libraries

import joblib
import  pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import cross_val_score
import config
import model_dispatcher
import os 

#read the data

df = pd.read_csv(config.TRAINING_FILE)

#feature engineering(remove features with low variance)

var_thresh = VarianceThreshold(threshold=0.1)
X = df.drop(["device_category"],axis=1)
y = df["device_category"]
var_thresh.fit(X)
var_thresh.get_support()

concol = [column for column in X.columns 
          if column not in X.columns[var_thresh.get_support()]]
X = X.drop(concol,axis=1)

#data preprocessing(standardization)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#splitting the data

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

#training the model

clf = model_dispatcher.models["rf"]
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("done with training, evaluating the model")

#evaluating the model

accuracy_score(y_test,y_pred) #accuracy score
print(f"Accuracy={accuracy_score}")

#cross validation
k = 10
scores = cross_val_score(clf, X_train, y_train, cv=k, scoring='accuracy')
mean_accuracy = scores.mean()
std_accuracy = scores.std()
print(scores)
print(f"Mean Accuracy: {mean_accuracy:.2f}")
print(f"Standard Deviation of Accuracy: {std_accuracy:.2f}")

# classification report 

print(classification_report(y_pred,y_test))

#saving model to disk

joblib.dump(clf, os.path.join(config.MODEL_OUTPUT, "RF.bin"))
print('model saved to disk')
