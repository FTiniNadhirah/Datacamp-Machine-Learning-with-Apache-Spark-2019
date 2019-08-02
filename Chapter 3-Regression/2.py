# Flight duration model: Just distance
# In this exercise you'll build a regression model to predict flight duration (the duration column).

# For the moment you'll keep the model simple, including only the distance of the flight (the km column) as a predictor.

# The data are in flights. The first few records are displayed in the terminal. These data have also been split into training and testing sets and are available as flights_train and flights_test.

# Instructions
# 100 XP
# Create a linear regression object. Specify the name of the label column. Fit it to the training data.
# Make predictions on the testing data.
# Create a regression evaluator object and use it to evaluate RMSE on the testing data.

from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data and take a look at the predictions
predictions = regression.transform(flights_test)
predictions.select('duration', 'prediction').show(5, False)

# Calculate the RMSE
RegressionEvaluator(labelCol='duration').evaluate(predictions)