# Exercise
# Exercise
# Build a Logistic Regression model
# You've already built a Decision Tree model using the flights data. Now you're going to create a Logistic Regression model on the same data.

# The objective is to predict whether a flight is likely to be delayed by at least 15 minutes (label 1) or not (label 0).

# Although you have a variety of predictors at your disposal, you'll only use the mon, depart and duration columns for the moment. These are numerical features which can immediately be used for a Logistic Regression model. You'll need to do a little more work before you can include categorical features. Stay tuned!

# The data have been split into training and testing sets and are available as flights_train and flights_test.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the class for creating a Logistic Regression classifier.
# Create a classifier object and train it on the training data.
# Make predictions for the testing data and create a confusion matrix.

# Import the logistic regression class
from pyspark.ml.classification import LogisticRegression

# Create a classifier object and train on training data
logistic = LogisticRegression().fit(flights_train)

# Create predictions for the testing data and show confusion matrix
prediction = logistic.transform(flights_test)
prediction.groupBy('label', 'prediction').count().show()
