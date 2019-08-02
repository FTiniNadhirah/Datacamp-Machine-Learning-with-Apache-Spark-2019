# Delayed flights with Gradient-Boosted Trees
# You've previously built a classifier for flights likely to be delayed using a Decision Tree. In this exercise you'll compare a Decision Tree model to a Gradient-Boosted Trees model.

# The flights data have been randomly split into flights_train and flights_test.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the classes required to create Decision Tree and Gradient-Boosted Tree classifiers.
# Create Decision Tree and Gradient-Boosted Tree classifiers. Train on the training data.
# Create an evaluator and calculate AUC on testing data for both classifiers. Which model performs better?
# Find the number of trees and the relative importance of features in the Gradient-Boosted Tree classifier.

from pyspark.ml.classification import DecisionTreeClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Create model objects and train on training data
tree = DecisionTreeClassifier().fit(flights_train)
gbt = GBTClassifier().fit(flights_train)

# Compare AUC on testing data
evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(tree.transform(flights_test))
evaluator.evaluate(gbt.transform(flights_test))

# Find the number of trees and the relative importance of features
print(gbt.getNumTrees)
print(gbt.featureImportances)