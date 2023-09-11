#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Training task 2: Weight
Write a function that takes summarizes the weight of all toys in the data set in gram.

SOLUTION
"""


weights = {
    "Fiesta": {"category": "Car", "weight": "1.2t"},
    "ExxonValdez": {"category": "tanker", "weight": "320t"},
    "Barbie": {"category": "toy", "weight": "0.000012t"},
    "Roxie": {"category": "dog", "weight": "0.019t"},
    "Lego-Brick": {"category": "toy", "weight": "0.0000015"}
}

def make_int_weight(str_weight): # change string to int and convert from tons to kilo
    itemweight = str_weight.replace("t", "") # remove literal from weight string
    itemweight = float(itemweight) # convert weight string into float value
    itemweight = itemweight * 1000000 # convert tons to grams
    itemweight = round(itemweight, 2) # round to max 2 digits after comma (optional)
    return (itemweight) # return clean weight in grams



def getweight():
    for item in weights: # iterate trought all items in the dict
        if weights[item]["category"] == "toy": # only take items into account if category "toy" applies
            weight = weights[item]["weight"] # get weight from selected items
            weight = make_int_weight(weight) # convert into grams as float value
            print (weight, type(weight)) # print weight value and show type to proof it's a float.
            toy_weight_list.append(weight) # add weight float value to list of weights for later sum up.



toy_weight_list = [] # create list of weights

getweight() # get weight values and add them to the list

toy_weight_sum = sum(toy_weight_list) # summarize values

print (toy_weight_sum) # print result





