# Flight duration model: Adding departure time
# In the previous exercise the departure time was bucketed and converted to dummy variables. Now you're going to include those dummy variables in a regression model for flight duration.

# The data are in flights. The km, org_dummy and depart_dummy columns have been assembled into features, where km is index 0, org_dummy runs from index 1 to 7 and depart_dummy from index 8 to 14.

# The data have been split into training and testing sets and a linear regression model, regression, has been built on the training data. Predictions have been made on the testing data and are available as predictions.

# Instructions
# 100 XP
# Find the RMSE for predictions on the testing data.
# Find the average time spent on the ground for flights departing from OGG between 21:00 and 24:00.
# Find the average time spent on the ground for flights departing from OGG between 00:00 and 03:00.
# Find the average time spent on the ground for flights departing from JFK between 00:00 and 03:00.

# Find the RMSE on testing data
from pyspark.ml.evaluation import RegressionEvaluator
RegressionEvaluator(labelCol='duration').evaluate(predictions)

# Average minutes on ground at OGG for flights departing between 21:00 and 24:00
avg_eve_ogg = regression.intercept
print(avg_eve_ogg)

# Average minutes on ground at OGG for flights departing between 00:00 and 03:00
avg_night_ogg = regression.intercept + regression.coefficients[8]
print(avg_night_ogg)

# Average minutes on ground at JFK for flights departing between 00:00 and 03:00
avg_night_jfk = regression.intercept + regression.coefficients[8] + regression.coefficients[3]
print(avg_night_jfk)