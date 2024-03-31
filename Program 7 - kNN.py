from collections import Counter
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            distances = [
                (self.__get_distance(x, x_train), y_train)
                for x_train, y_train in zip(self.X_train, self.y_train)
            ]

            distances.sort()
            nn = distances[: self.k]

            class_votes = Counter([label for _, label in nn])
            predicted_class = max(class_votes, key=class_votes.get)
            predictions.append(predicted_class)

        return predictions

    def __get_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))


knn = KNNClassifier(k=3)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

acc = accuracy_score(y_test, predictions)
print(f"Test Accuracy: {acc*100:.4f}%")
print(classification_report(y_test, predictions))
