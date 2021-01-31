'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

# There are 1830 seconds in 30 minutes and 30 seconds
miles_per_second = 10 / 1830
# There are 3600 seconds in one hour - this next line calculates the average speed in miles per hour
miles_per_hour = miles_per_second * 3600
# One mile is 1.6 km
km_per_hour = miles_per_hour * 1.6
print(km_per_hour)
