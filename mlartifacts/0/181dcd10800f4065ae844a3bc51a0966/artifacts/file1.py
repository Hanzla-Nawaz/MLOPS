import mlflow
mlflow.set_tracking_uri("http://localhost:5000/")
import mlflow.sklearn
mlflow.sklearn.autolog()

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load iris dataset which has both features and targets
load_data = load_iris()

print(load_data.keys())
print(load_data.target.shape)
print(load_data.target)
print(load_data.target_names)
print(load_data.data.shape)
print(load_data.data[0])

X = load_data.data
y = load_data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(X_train[0])
print(y_train[0])
print(X_test[0])

max_depth = [None, 5]
n_estimators = [100]

for md in max_depth:
    for ne in n_estimators:
        with mlflow.start_run():
            rf = RandomForestClassifier(max_depth=md, n_estimators=ne)
            rf.fit(X_train, y_train)
            y_pred = rf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            mlflow.log_param("max_depth", md)
            mlflow.log_param("n_estimators", ne)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.sklearn.log_model(rf, "model")
            print(f"max_depth: {md}, n_estimators: {ne}, accuracy: {accuracy}")



cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

plt.savefig("confusion_matrix.png")

mlflow.log_artifact("confusion_matrix.png")
mlflow.log_artifact(__file__)




