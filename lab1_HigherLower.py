# lab1_HigherLower.py

# Brianna Drew
# January 19, 2021
# ID: #0622446
# Lab #1, Part #2

# import required modules
import time
import random

higher = 0 # counter for numbers greater than 5
lower = 0 # counter for numbers less than or equal to 5

# seed the random number generator
random.seed(int(round(time.time()*1000)))

# generate 1,000 random integers
for i in range (0,1000):
    # generate random number from 1 to 10
    number = random.randint(1,10)
    # determine whether random number generated is greater than 5 or not
    if  number >  5:
        # increment counter for higher
        higher += 1
    else:
        # increment counter for lower
        lower += 1

# print results
print("RESULTS:")
print("--------")
print("Numbers from 1-5: ", lower)
print("Numbers from 6-10: ", higher)