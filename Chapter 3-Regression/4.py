# Flight duration model: Adding origin airport
# Some airports are busier than others. Some airports are bigger than others too. Flights departing from large or busy airports are likely to spend more time taxiing or waiting for their takeoff slot. So it stands to reason that the duration of a flight might depend not only on the distance being covered but also the airport from which the flight departs.

# You are going to make the regression model a little more sophisticated by including the departure airport as a predictor.

# These data have been split into training and testing sets and are available as flights_train and flights_test. The origin airport, stored in the org column, has been indexed into org_idx, which in turn has been one-hot encoded into org_dummy. The first few records are displayed in the terminal.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Split the data into training (80%) and testing (20%) sets. Use a random number seed of 13 for repeatability.
# Fit a linear regression model to the training data.
# Make predictions for the testing data.
# Calculate the RMSE for predictions on the testing data.


from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Create a regression object and train on training data
regression = LinearRegression(labelCol='duration').fit(flights_train)

# Create predictions for the testing data
predictions = regression.transform(flights_test)

# Calculate the RMSE on testing data
RegressionEvaluator(labelCol='duration').evaluate(predictions)