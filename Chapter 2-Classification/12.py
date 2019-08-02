# Exercise
# Exercise
# Training a spam classifier
# The SMS data have now been prepared for building a classifier. Specifically, this is what you have done:

# removed numbers and punctuation
# split the messages into words (or "tokens")
# removed stop words
# applied the hashing trick and
# converted to a TF-IDF representation.
# Next you'll need to split the TF-IDF data into training and testing sets. Then you'll use the training data to fit a Logistic Regression model and finally evaluate the performance of that model on the testing data.

# The data are stored in sms and LogisticRegression has been imported for you.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Split the data into training and testing sets in a 4:1 ratio. Set the random number seed to 13 to ensure repeatability.
# Create a LogisticRegression object and fit it to the training data.
# Generate predictions on the testing data.
# Use the predictions to form a confusion matrix.

# Split the data into training and testing sets
sms_train, sms_test = sms.randomSplit([0.8, 0.2], seed=13)

# Fit a Logistic Regression model to the training data
logistic = LogisticRegression(regParam=0.2).fit(sms_train)

# Make predictions on the testing data
prediction = logistic.transform(sms_test)

# Create a confusion matrix, comparing predictions to known labels
prediction.groupBy('label', 'prediction').count().show()