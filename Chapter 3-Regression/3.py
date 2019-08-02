# Interpreting the coefficients
# The linear regression model for flight duration as a function of distance takes the form

# duration=α+β×distance
# where

# α — intercept (component of duration which does not depend on distance) and
# β — coefficient (rate at which duration increases as a function of distance; also called the slope).
# By looking at the coefficients of your model you will be able to infer

# how much of the average flight duration is actually spent on the ground and
# what the average speed is during a flight.
# The linear regression model is available as regression.

# Instructions
# 100 XP
# Instructions
# 100 XP
# What's the intercept?
# What are the coefficients? This is a vector.
# Extract the slope for distance by indexing into the vector.
# Find the average speed in km per hour.

# Intercept (average minutes on ground)
inter = regression.intercept
print(inter)

# Coefficients
coefs = regression.coefficients
print(coefs)

# Average minutes per km
minutes_per_km = regression.coefficients[0]
print(minutes_per_km)

# Average speed in km per hour
avg_speed = 60 / minutes_per_km
print(avg_speed)