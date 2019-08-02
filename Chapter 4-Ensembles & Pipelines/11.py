# Evaluating Random Forest
# In this final exercise you'll be evaluating the results of cross-validation on a Random Forest model.

# The following have already been created:

# cv - a cross-validator which has already been fit to the training data
# evaluator — a BinaryClassificationEvaluator object and
# flights_test — the testing data.
# Instructions
# 100 XP
# Instructions
# 100 XP
# Retrieve a list of average AUC metrics across all models in the parameter grid.
# What is the average AUC for the best model? This will be the largest AUC in the list.
# Find the value of the maxDepth and featureSubsetStrategy parameters for the best model.
# Calculate the AUC for the best model predictions on the testing data.

# Average AUC for each parameter combination in grid
avg_auc = cv.avgMetrics

# Average AUC for the best model
best_model_auc = max(cv.avgMetrics)

# What's the optimal parameter value?
opt_max_depth = cv.bestModel.explainParam('maxDepth')
opt_feat_substrat = cv.bestModel.explainParam('featureSubsetStrategy')

# AUC for best model on testing data
best_auc = evaluator.evaluate(cv.transform(flights_test))