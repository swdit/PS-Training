#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Training task 3: NumbersExeption from P to S

Write a program that prints the integers from 1 to 100 (inclusive).

But:
for multiples of three,   print "Fizz" instead of the number;
for multiples of five,   print "Buzz" instead of the number;
for multiples of both three and five, print "FizzBuzz" instead of the number.

But 2:
give me three different solutions


SOLUTION
"""


# Solution 1:

def multicheck(number, divider):
     if number%divider == 0:
        return True
     else:
        return False


for n in range(1, 101):
    if multicheck(n, 3) and multicheck(n, 5):
        print ("FizzBuzz")
    elif multicheck(n, 3):
        print ("Fizz")
    elif multicheck(n, 5):
        print ("Buzz")
    else:
        print (n)


# Solution 2:


def multicheck2(number, divider):
    quotient = number/divider
    quotient = str(quotient)
    if ".0" in quotient:
        return True
    else:
        return False

for n in range(1, 101):
    if multicheck2(n, 3) and multicheck2(n, 5):
        print ("FizzBuzz")
    elif multicheck2(n, 3):
        print ("Fizz")
    elif multicheck2(n, 5):
        print ("Buzz")
    else:
        print (n)


# Solution 3:

multicheck3 = lambda number: ("FizzBuzz" if number%5 == 0 and number%3 == 0 else ("Fizz" if number%3 == 0 else ("Buzz" if number%5 == 0 else number)))

for n in range(1, 101):
    print(multicheck3(n))




