# Exercise
# Exercise
# Stop words and hashing
# The next steps will be to remove stop words and then apply the hashing trick, converting the results into a TF-IDF.

# A quick reminder about these concepts:

# The hashing trick provides a fast and space-efficient way to map a very large (possibly infinite) set of items (in this case, all words contained in the SMS messages) onto a smaller, finite number of values.
# The TF-IDF matrix reflects how important a word is to each document. It takes into account both the frequency of the word within each document but also the frequency of the word across all of the documents in the collection.
# The tokenized SMS data are stored in sms in a column named words. You've cleaned up the handling of spaces in the data so that the tokenized text is neater.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the StopWordsRemover, HashingTF and IDF classes.
# Create a StopWordsRemover object (input column words, output column terms). Apply to sms.
# Create a HashingTF object (input results from previous step, output column hash). Apply to wrangled.
# Create an IDF object (input results from previous step, output column features). Apply to wrangled.

from pyspark.ml.feature import StopWordsRemover, HashingTF, IDF

# Remove stop words.
wrangled = StopWordsRemover(inputCol='words', outputCol='terms')\
      .transform(sms)

# Apply the hashing trick
wrangled = HashingTF(inputCol='terms', outputCol='hash', numFeatures=1024)\
      .transform(wrangled)

# Convert hashed symbols to TF-IDF
tf_idf = IDF(inputCol='hash', outputCol='features')\
      .fit(wrangled).transform(wrangled)
      
tf_idf.select('terms', 'features').show(4, truncate=False)