# aaExercise
# Exercise
# Encoding flight origin
# The org column in the flights data is a categorical variable giving the airport from which a flight departs.

# ORD — O'Hare International Airport (Chicago)
# SFO — San Francisco International Airport
# JFK — John F Kennedy International Airport (New York)
# LGA — La Guardia Airport (New York)
# SMF — Sacramento
# SJC — San Jose
# TUS — Tucson International Airport
# OGG — Kahului (Hawaii)
# Obviously this is only a small subset of airports. Nevertheless, since this is a categorical variable, it needs to be one-hot encoded before it can be used in a regression model.

# The data are in a variable called flights. You have already used a string indexer to create a column of indexed values corresponding to the strings in org.

# Note:: You might find it useful to revise the slides from the lessons in the Slides panel next to the IPython Shell.

# Instructions
# 100 XP
# Import the one-hot encoder class.
# Create an one-hot encoder instance, naming the output column 'org_dummy'.
# Apply the one-hot encoder to the flights data.
# Generate a summary of the mapping from categorical values to binary encoded dummy variables. Include only unique values and order by org_idx.


# Import the one hot encoder class
from pyspark.ml.feature import OneHotEncoderEstimator

# Create an instance of the one hot encoder
onehot = OneHotEncoderEstimator(inputCols=['org_idx'], outputCols=['org_dummy'])

# Apply the one hot encoder to the flights data
onehot = onehot.fit(flights)
flights_onehot = onehot.transform(flights)

# Check the results
flights_onehot.select('org', 'org_idx', 'org_dummy').distinct().sort('org_idx').show()