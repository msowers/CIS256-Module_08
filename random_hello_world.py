"""
Matt Sowers
Module 08 Lab Assignment: Part B

This script picks a random number from 1-10 and then print "Hello world" the amount of times the random number was.
"""
# import random
import random

# set random number and random number from 1-10
random_number = random.randint(1, 10)

# print Hello World! tha random number of times
for i in range(random_number):
    print("Hello world!")