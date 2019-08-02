# Dissecting the best flight duration model
# You just set up a CrossValidator to find good parameters for the linear regression model predicting flight duration.

# Now you're going to take a closer look at the resulting model, split out the stages and use it to make predictions on the testing data.

# The following have already been created:

# cv — a trained CrossValidatorModel object and
# evaluator — a RegressionEvaluator object.
# The flights data have been randomly split into flights_train and flights_test.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Retrieve the best model.
# Look at the stages in the best model.
# Isolate the linear regression stage and extract its parameters.
# Use the best model to generate predictions on the testing data and calculate the RMSE.

# Get the best model from cross validation
best_model = cv.bestModel

# Look at the stages in the best model
print(best_model.stages)

# Get the parameters for the LinearRegression object in the best model
best_model.stages[3].extractParamMap()

# Generate predictions on testing data using the best model then calculate RMSE
predictions = best_model.transform(flights_test)
evaluator.evaluate(predictions)