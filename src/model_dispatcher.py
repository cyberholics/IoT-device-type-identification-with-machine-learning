from sklearn.ensemble import RandomForestClassifier

hyperparameters = {
    'bootstrap': False,
    'max_depth': None,
    'min_samples_leaf': 1,
    'min_samples_split': 5,
    'n_estimators': 200
}

models = {
    "rf": RandomForestClassifier(**hyperparameters)
}
