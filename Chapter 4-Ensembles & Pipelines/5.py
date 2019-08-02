# Cross validating flight duration model pipeline
# The cross-validated model that you just built was simple, using km alone to predict duration.

# Another important predictor of flight duration is the origin airport. Flights generally take longer to get into the air from busy airports. Let's see if adding this predictor improves the model!

# In this exercise you'll add the org field to the model. However, since org is categorical, there's more work to be done before it can be included: it must first be transformed to an index and then one-hot encoded before being assembled with km and used to build the regression model. We'll wrap these operations up in a pipeline.

# The following objects have already been created:

# params — an empty parameter grid
# evaluator — a regression evaluator
# regression — a LinearRegression object with labelCol='duration'.
# All of the required classes have already been imported.

# Instructions
# 100 XP
# Create a string indexer. Specify the input and output fields as org and org_idx.
# Create a one-hot encoder. Name the output field org_dummy.
# Assemble the km and org_dummy fields into a single field called features.
# Create a pipeline using the following operations: string indexer, one-hot encoder, assembler and linear regression. Use this to create a cross-validator.


# Create an indexer for the org field
indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# Create an one-hot encoder for the indexed org field
onehot = OneHotEncoderEstimator(inputCols=['org_idx'], outputCols=['org_dummy'])

# Assemble the km and one-hot encoded fields
assembler = VectorAssembler(inputCols=['km', 'org_dummy'], outputCol='features')

# Create a pipeline and cross-validator.
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])
cv = CrossValidator(estimator=pipeline,
                    estimatorParamMaps=params,
                    evaluator=evaluator)