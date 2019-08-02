# Exercise
# Exercise
# Build a Decision Tree
# Now that you've split the flights data into training and testing sets, you can use the training set to fit a Decision Tree model.

# The data are available as flights_train and flights_test.

# NOTE: It will take a few seconds for the model to train... please be patient!

# Instructions
# 100 XP
# Import the class for creating a Decision Tree classifier.
# Create a classifier object and fit it to the training data.
# Make predictions for the testing data and take a look at the predictions.

# Import the Decision Tree Classifier class
from pyspark.ml.classification import DecisionTreeClassifier

# Create a classifier object and fit to the training data
tree = DecisionTreeClassifier()
tree_model = tree.fit(flights_train)

# Create predictions for the testing data and take a look at the predictions
prediction = tree_model.transform(flights_test)
prediction.select('label', 'prediction', 'probability').show(5, False)