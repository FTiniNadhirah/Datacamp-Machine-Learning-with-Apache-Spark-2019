# Evaluate the Logistic Regression model
# Accuracy is generally not a very reliable metric because it can be biased by the most common target class.

# There are two other useful metrics:

# precision and
# recall.
# Check the slides for this lesson to get the relevant expressions.

# Precision is the proportion of positive predictions which are correct. For all flights which are predicted to be delayed, what proportion is actually delayed?

# Recall is the proportion of positives outcomes which are correctly predicted. For all delayed flights, what proportion is correctly predicted by the model?

# The precision and recall are generally formulated in terms of the positive target class. But it's also possible to calculate weighted versions of these metrics which look at both target classes.

# The components of the confusion matrix are available as TN, TP, FN and FP, as well as the object prediction.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Find the precision and recall.
# Create a multi-class evaluator and evaluate weighted precision.
# Create a binary evaluator and evaluate AUC.

from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator

# Calculate precision and recall
precision = TP / (TP + FP)
recall = TP / (TP + FN)
print('precision = {:.2f}\nrecall    = {:.2f}'.format(precision, recall))

# Find weighted precision
multi_evaluator = MulticlassClassificationEvaluator()
weighted_precision = multi_evaluator.evaluate(prediction, {multi_evaluator.metricName: "weightedPrecision"})

# Find AUC
binary_evaluator = BinaryClassificationEvaluator()
auc = binary_evaluator.evaluate(prediction, {binary_evaluator.metricName: "areaUnderROC"})