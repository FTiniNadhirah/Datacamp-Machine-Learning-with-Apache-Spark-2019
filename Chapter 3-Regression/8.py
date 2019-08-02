# Flight duration model: More features!
# Let's add more features to our model. This will not necessarily result in a better model. Adding some features might improve the model. Adding other features might make it worse.

# More features will always make the model more complicated and difficult to interpret.

# These are the features you'll include in the next model:

# km
# org (origin airport, one-hot encoded, 8 levels)
# depart (departure time, binned in 3 hour intervals, one-hot encoded, 8 levels)
# dow (departure day of week, one-hot encoded, 7 levels) and
# mon (departure month, one-hot encoded, 12 levels).
# These have been assembled into the features column, which is a sparse representation of 32 columns (remember one-hot encoding produces a number of columns which is one fewer than the number of levels).

# The data are available as flights, randomly split into flights_train and flights_test. The object predictions is also available.

# Instructions
# 100 XP
# Fit a linear regression model to the training data.
# Generate predictions for the testing data.
# Calculate the RMSE on the testing data.
# Look at the model coefficients. Are any of them zero?

from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Fit linear regression model to training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Make predictions on testing data
predictions = regression.transform(flights_test)

# Calculate the RMSE on testing data
rmse = RegressionEvaluator(labelCol='duration').evaluate(predictions)
print("The test RMSE is", rmse)

# Look at the model coefficients
coeffs = regression.coefficients
print(coeffs)