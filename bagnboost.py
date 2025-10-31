# 🌳 Ensemble Learning: Bagging and Boosting

from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# ============================
# 1️⃣ Bagging Classifier
# ============================
bag_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),  # updated parameter name
    n_estimators=10,                     # number of trees
    random_state=1
)
bag_model.fit(X_train, y_train)

# Prediction and Evaluation
y_pred_bag = bag_model.predict(X_test)
print("🌲 Bagging Accuracy:", accuracy_score(y_test, y_pred_bag))

# ============================
# 2️⃣ Boosting (AdaBoost)
# ============================
boost_model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),  # weak learner
    n_estimators=10,
    learning_rate=1.0,
    random_state=1
)
boost_model.fit(X_train, y_train)

# Prediction and Evaluation
y_pred_boost = boost_model.predict(X_test)
print("⚡ Boosting Accuracy:", accuracy_score(y_test, y_pred_boost))
