# SMS spam pipeline
# You haven't looked at the SMS data for quite a while. Last time we did the following:

# split the text into tokens
# removed stop words
# applied the hashing trick
# converted the data from counts to IDF and
# trained a linear regression model.
# Each of these steps was done independently. This seems like a great application for a pipeline!

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create an object for splitting text into tokens.
# Create an object to remove stop words. Rather than explicitly giving the input column name, use the getOutputCol() method on the previous object.
# Create objects for applying the hashing trick and transforming the data into a TF-IDF. Use the getOutputCol() method again.
# Create a pipeline which wraps all of the above steps as well as an object to create a Logistic Regression model.

from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF

# Break text into tokens at non-word characters
tokenizer = Tokenizer(inputCol='text', outputCol='words')

# Remove stop words
remover = StopWordsRemover(inputCol=tokenizer.getOutputCol(), outputCol='terms')

# Apply the hashing trick and transform to TF-IDF
hasher = HashingTF(inputCol=remover.getOutputCol(), outputCol="hash")
idf = IDF(inputCol=hasher.getOutputCol(), outputCol="features")

# Create a logistic regression object and add everything to a pipeline
logistic = LogisticRegression()
pipeline = Pipeline(stages=[tokenizer, remover, hasher, idf, logistic])