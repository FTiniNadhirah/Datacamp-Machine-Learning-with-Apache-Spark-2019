##Loading flights data
##In this exercise you're going to load some airline flight data from a CSV file. To ensure that the exercise runs quickly these data have been trimmed down to only 50 000 records. You can get a larger dataset in the same format here.
##
##Notes on CSV format:
##
##fields are separated by a comma (this is the default separator) and
##missing data are denoted by the string 'NA'.
##Data dictionary:
##
##mon — month (integer between 1 and 12)
##dom — day of month (integer between 1 and 31)
##dow — day of week (integer; 1 = Monday and 7 = Sunday)
##org — origin airport (IATA code)
##mile — distance (miles)
##carrier — carrier (IATA code)
##depart — departure time (decimal hour)
##duration — expected duration (minutes)
##delay — delay (minutes)
##pyspark has been imported for you and the session has been initialized.
##
##Note: The data have been aggressively down-sampled.
##
##Instructions
##100 XP
##Instructions
##100 XP
##Read data from a CSV file called 'flights.csv'. Assign data types to columns automatically. Deal with missing data.
##How many records are in the data?
##Take a look at the first five records.
##What data types have been assigned to the columns? Do these look correct?
# Read data from CSV file
flights = spark.read.csv('flights.csv',
                         sep=',',
                         header=True,
                         inferSchema=True,
                         nullValue='NA')

# Get number of records
print("The data contain %d records." % flights.count())

# View the first five records
flights.show(5)

# Check column data types
flights.dtypes
