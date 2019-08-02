# Punctuation, numbers and tokens
# At the end of the previous chapter you loaded a dataset of SMS messages which had been labeled as either "spam" (label 1) or "ham" (label 0). You're now going to use those data to build a classifier model.

# But first you'll need to prepare the SMS messages as follows:

# remove punctuation and numbers
# tokenize (split into individual words)
# remove stop words
# apply the hashing trick
# convert to TF-IDF representation.
# In this exercise you'll remove punctuation and numbers, then tokenize the messages.

# The SMS data are available as sms.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the function to replace regular expressions and the feature to tokenize.
# Replace all punctuation characters from the text column with a space. Do the same for all numbers in the text column.
# Split the text column into tokens. Name the output column words.


# Import the necessary functions
from pyspark.sql.functions import regexp_replace
from pyspark.ml.feature import Tokenizer

# Remove punctuation (REGEX provided) and numbers
wrangled = sms.withColumn('text', regexp_replace(sms.text, '[_():;,.!?\\-]', ' '))
wrangled = wrangled.withColumn('text', regexp_replace(wrangled.text, '[0-9]', ' '))

# Merge multiple spaces
wrangled = wrangled.withColumn('text', regexp_replace(wrangled.text, ' +', ' '))

# Split the text into words
wrangled = Tokenizer(inputCol='text', outputCol='words').transform(wrangled)

wrangled.show(4, truncate=False)