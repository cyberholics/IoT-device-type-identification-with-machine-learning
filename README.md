# IoT-device-type-identification-with-machine-learning


An IoT device is any device that is connected to the internet and can collect or transmit data. Hackers can add their own IoT device, or a malicious IoT device, to an organization's network. Once the hacker has added their own IoT device to the network, they can use it to gain access to other devices on the network, steal data, or launch attacks.
Therefore, it is important to identify when a new IoT device has been added to a network and understand what kind of device it is.

Machine learning can be used as a network security solution to identify the types of IoT devices. Machine learning algorithms can be trained on data from known IoT devices to learn the characteristics of these devices. Once the machine learning algorithm has been trained, it can be used to identify new IoT devices that connect to the network.

## Data used
The power of a machine learning solution lies in its training data. Therefore, in this project, I took advantage of datasets generated from IoT device network traffic analysis because, unlike data generated from device fingerprinting, network traffic analysis data cannot be spoofed.
The data was gotten from [Kaggle](https://www.kaggle.com/datasets/fanbyprinciple/iot-device-identification). 

## Project files and folders explained
- **Input:** This folder contains the data used for this project
- **Notebook:** This folder contains the Jupyter Notebook used for Exploratory data analysis, data preprocessing, feature engineering and modeling (Check it out to see how I came up with the final model)

## Project Summary
- I got IoT device network traffic analysis data from Kaggle; the data contains network traffic analysis for the following IoT devices:
  ```security camera, TV, smoke detector, thermostat, water sensor, watch, baby monitor, motion sensor, lights, socket```
- I performed feature engineering on the data by removing features with low variance. Features with low variance tend to have constant values and do not contribute meaningfully to the model's learning process
- I pre-processed the data by performing standardization. Standardization is a method that transforms the training data to have a mean of 0 and a variance of 1.
In standardization, the goal is to transform the data in such a way that it has a mean (average) of 0 and a variance (standard deviation squared) of 1. This transformation gives the data a standard normal distribution, which can be beneficial for the machine learning algorithm
- I used different algorithms (Logistic Regression, Random Forest Classifier, and Gradient Boosting Classifier) to build a model. Among these algorithms, I achieved the best performance with the Random Forest Classifier. Therefore, I selected the Random Forest Classifier as my final model
- I evaluated the final model using the accuracy score and a cross-validation technique. I achieved 90% accuracy on the model, with an average accuracy of 86% across 10 folds of cross-validation; this indicated the model is not overfitting

[Technical article about this solution](https://dev.to/cyber_holics/how-to-identify-iot-devices-with-machine-learning-3j32)
