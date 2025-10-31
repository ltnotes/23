# CART Algorithm using scikit-learn

from sklearn.tree import DecisionTreeClassifier, export_text

# Sample dataset: [Age, Income]
X = [
    [25, 40000],
    [35, 60000],
    [45, 80000],
    [20, 20000],
    [50, 90000]
]

# Target: Buys (0 = No, 1 = Yes)
y = [0, 0, 1, 0, 1]

# Create and train CART model
model = DecisionTreeClassifier(criterion='gini')  # CART uses Gini impurity
model.fit(X, y)

# Predict
pred = model.predict([[30, 50000]])
print("Prediction for [30, 50000]:", pred[0])

# Display decision rules
tree_rules = export_text(model, feature_names=["Age", "Income"])
print("\nDecision Tree Rules:\n", tree_rules)
