# Flight duration model: Pipeline model
# You're now ready to put those stages together in a pipeline.

# You'll construct the pipeline and then train the pipeline on the training data. This will apply each of the individual stages in the pipeline to the training data in turn. None of the stages will be exposed to the testing data at all: there will be no leakage!

# Once the entire pipeline has been trained it will then be used to make predictions on the testing data.

# The data are available as flights, which has been randomly split into flights_train and flights_test.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the class for creating a pipeline.
# Create a pipeline object and specify the indexer, onehot, assembler and regression stages, in this order.
# Train the pipeline on the training data.
# Make predictions on the testing data.

# Import class for creating a pipeline
from pyspark.ml import Pipeline

# Construct a pipeline
pipeline = Pipeline(stages=[indexer, onehot, assembler, regression])

# Train the pipeline on the training data
pipeline = pipeline.fit(flights_train)

# Make predictions on the testing data
predictions = pipeline.transform(flights_test)