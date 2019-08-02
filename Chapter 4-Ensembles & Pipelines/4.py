# Cross validating simple flight duration model
# You've already built a few models for predicting flight duration and evaluated them with a simple train/test split. However, cross-validation provides a much better way to evaluate model performance.

# In this exercise you're going to train a simple model for flight duration using cross-validation. Travel time is usually strongly correlated with distance, so using the km column alone should give a decent model.

# The data have been randomly split into flights_train and flights_test.

# The following classes have already been imported: LinearRegression, RegressionEvaluator, ParamGridBuilder and CrossValidator.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create an empty parameter grid.
# Create objects for building and evaluating a linear regression model. The model should predict the "duration" field.
# Create a cross-validator object. Provide values for the estimator, estimatorParamMaps and evaluator arguments. Choose 5-fold cross validation.
# Train and test the model across multiple folds of the training data.
# Create an empty parameter grid
params = ParamGridBuilder().build()

# Create objects for building and evaluating a regression model
regression = LinearRegression(labelCol='duration')
evaluator = RegressionEvaluator(labelCol='duration')

# Create a cross validator
cv = CrossValidator(estimator=regression, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)

# Train and test model on multiple folds of the training data
cv = cv.fit(flights_train)

# NOTE: Since cross-validation builds multiple models, the fit() method can take a little while to complete.