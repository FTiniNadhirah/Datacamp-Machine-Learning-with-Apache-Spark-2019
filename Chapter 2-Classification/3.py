##Categorical columns
##In the flights data there are two columns, carrier and org, which hold categorical data. You need to transform those columns into indexed numerical values.
##
##Instructions
##100 XP
##Import the appropriate class and create an indexer object to transform the carrier column from a string to an numeric index.
##Prepare the indexer object on the flight data.
##Use the prepared indexer to create the numeric index column.
##Repeat the process for the org column.
from pyspark.ml.feature import StringIndexer

# Create an indexer
indexer = StringIndexer(inputCol='carrier', outputCol='carrier_idx')

# Indexer identifies categories in the data
indexer_model = indexer.fit(flights)

# Indexer creates a new column with numeric index values
flights_indexed = indexer_model.transform(flights)

# Repeat the process for the other categorical feature
flights_indexed = StringIndexer(inputCol='org', outputCol='org_idx').fit(flights_indexed).transform(flights_indexed)
