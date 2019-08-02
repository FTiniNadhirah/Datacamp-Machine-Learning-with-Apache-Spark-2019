# Exercise
# Exercise
# Interpreting coefficients
# Remember that origin airport, org, has eight possible values (ORD, SFO, JFK, LGA, SMF, SJC, TUS and OGG) which have been one-hot encoded to seven dummy variables in org_dummy.

# The values for km and org_dummy have been assembled into features, which has eight columns with sparse representation. Column indices in features are as follows:

# 0 — km
# 1 — ORD
# 2 — SFO
# 3 — JFK
# 4 — LGA
# 5 — SMF
# 6 — SJC and
# 7 — TUS.
# Note that OGG does not appear in this list because it is the reference level for the origin airport category.

# In this exercise you'll be using the intercept and coefficients attributes to interpret the model.

# The coefficients attribute is a list, where the first element indicates how flight duration changes with flight distance.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Find the average speed in km per hour. This will be different to the value that you got earlier because your model is now more sophisticated.
# What's the average time on the ground at OGG?
# What's the average time on the ground at JFK?
# What's the average time on the ground at LGA?


# Average speed in km per hour
avg_speed_hour = 60 / regression.coefficients[0]
print(avg_speed_hour)

# Average minutes on ground at OGG
inter = regression.intercept
print(inter)

# Average minutes on ground at JFK
avg_ground_jfk = inter + regression.coefficients[3]
print(avg_ground_jfk)

# Average minutes on ground at LGA
avg_ground_lga = inter + regression.coefficients[4]
print(avg_ground_lga)