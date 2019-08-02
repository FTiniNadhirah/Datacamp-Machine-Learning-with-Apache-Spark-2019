##Loading SMS spam data
##You've seen that it's possible to infer data types directly from the data. Sometimes it's convenient to have direct control over the column types. You do this by defining an explicit schema.
##
##The file sms.csv contains a selection of SMS messages which have been classified as either 'spam' or 'ham'. These data have been adapted from the UCI Machine Learning Repository. There are a total of 5574 SMS, of which 747 have been labelled as spam.
##
##Notes on CSV format:
##
##no header record and
##fields are separated by a semicolon (this is not the default separator).
##Data dictionary:
##
##id — record identifier
##text — content of SMS message
##label — spam or ham (integer; 0 = ham and 1 = spam)
##Instructions
##100 XP
##Instructions
##100 XP
##Specify the data schema, giving columns names ('id', 'text' and 'label') and column types.
##Read data from a delimited file called 'sms.csv'.
##Print the schema for the resulting DataFrame.

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Specify column names and types
schema = StructType([
    StructField("id", IntegerType()),
    StructField("text", StringType()),
    StructField("label", IntegerType())
])

# Load data from a delimited file
sms = spark.read.csv("sms.csv", sep=';', header=False, schema=schema)

# Print schema of DataFrame
sms.printSchema()
