from collections import defaultdict
import math
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target
print(X[:2])
print(y[:5])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")


class NaiveBayesClassifier:
    def __init__(self):
        self.class_p = defaultdict(int)
        self.feature_p = defaultdict(lambda: defaultdict(int))
        self.unique_f = set()

    def fit(self, X_train, y_train):
        n = len(y_train)

        for i in range(n):
            c = y_train[i]
            self.class_p[c] += 1

            features = self.__preprocess(X_train[i])
            for f in features:
                self.feature_p[c][f] += 1
                self.unique_f.add(f)

        v = len(self.unique_f)
        for c in self.class_p:
            N = sum(self.feature_p[c].values())
            for f in self.unique_f:
                Nc = self.feature_p[c][f]
                self.feature_p[c][f] = (Nc + 1) / (N + v)

        for c in self.class_p:
            self.class_p[c] /= n

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            test_features = self.__preprocess(x)
            scores = {}

            v = len(self.unique_f)
            for c in self.class_p:
                score = math.log(self.class_p[c])
                for f in test_features:
                    if f in self.feature_p[c]:
                        score += math.log(self.feature_p[c][f])
                    else:
                        N = sum(self.feature_p[c].values())
                        score += math.log(1 / (N + v))

                scores[c] = score

            predicted_class = max(scores, key=scores.get)
            predictions.append(predicted_class)

        return predictions

    def __preprocess(self, x):
        return [str(i) for i in x]

nb = NaiveBayesClassifier()
nb.fit(X_train, y_train)

predictions = nb.predict(X_test)

acc = accuracy_score(y_test, predictions)
print(f"Test Accuracy: {acc*100:.4f}%")
print(classification_report(y_test, predictions))
