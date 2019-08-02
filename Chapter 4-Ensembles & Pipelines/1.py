# Exercise
# Exercise
# Flight duration model: Pipeline stages
# You're going to create the stages for the flights duration model pipeline. You will use these in the next exercise to build a pipeline and to create a regression model.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create an indexer to convert the 'org' column into an indexed column called 'org_idx'.
# Create a one-hot encoder to convert the 'org_idx' and 'dow' columns into dummy variable columns called 'org_dummy' and 'dow_dummy'.
# Create an assembler which will combine the 'km' column with the two dummy variable columns. The output column should be called 'features'.
# Create a linear regression object to predict flight duration.
# Note:: You might find it useful to revisit the slides from the lessons in the Slides panel next to the IPython Shell.

# Convert categorical strings to index values
indexer = StringIndexer(inputCol='org', outputCol='org_idx')

# One-hot encode index values
onehot = OneHotEncoderEstimator(
    inputCols=['org_idx', 'dow'],
    outputCols=['org_dummy', 'dow_dummy']
)

# Assemble predictors into a single column
assembler = VectorAssembler(inputCols=['km', 'org_dummy', 'dow_dummy'], outputCol='features')

# A linear regression object
regression = LinearRegression(labelCol='duration')