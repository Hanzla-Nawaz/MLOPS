from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
import pandas as pd
import mlflow

# Explicitly set the tracking URI to the local mlruns directory (project root)
mlflow.set_tracking_uri("file:///M:/working_25/Practical/Practical/MLOPS/mlruns")

# Diagnostic: List all experiments using workaround for very old MLflow
from mlflow.tracking import MlflowClient
client = MlflowClient()
for i in range(10):
    try:
        exp = client.get_experiment(str(i))
        print(f"Name: {exp.name}, ID: {exp.experiment_id}, Location: {exp.artifact_location}")
    except Exception as e:
        pass  # skip if not found

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [10, 50, 90],
    'max_depth': [None, 10, 50 ,90]
}

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

'''grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(best_params)
print(best_score)'''

'''mlflow.set_experiment('breast-cancer-rf-hp')
with mlflow.start_run():
    grid_search.fit(X_train, y_train)
    '''

# here we use 12 combinations but in mlflow we have best one 
# how to log all child runs


mlflow.set_experiment('breast-cancer-rf-child')

with mlflow.start_run(run_name="parent_run") as parent:
    grid_search.fit(X_train, y_train)

    # Log all child runs (all parameter combinations)
    for i in range(len(grid_search.cv_results_['params'])):
        with mlflow.start_run(run_name=f"child_run_{i}", nested=True):
            mlflow.log_params(grid_search.cv_results_['params'][i])
            mlflow.log_metric("accuracy", grid_search.cv_results_["mean_test_score"][i])

    # Log the best run in the parent
    best_params = grid_search.best_params_
    best_score = grid_search.best_score_
    mlflow.log_params(best_params)
    mlflow.log_metric("accuracy", best_score)

    train_df= X_train.copy()
    train_df['target'] = y_train

    train_df = mlflow.data.from_pandas(train_df)
    mlflow.log_input(train_df, "training")

    test_df= X_test.copy()
    test_df['target'] = y_test

    test_df = mlflow.data.from_pandas(test_df)
    mlflow.log_input(test_df, "training")

    mlflow.log_artifact(__file__)

    mlflow.sklearn.log_model(grid_search.best_estimator_,"random_forest")

    mlflow.set_tag("author", "Hanzla Nawaz")

    print(best_params)
    print(best_score)
    

        
