#!/usr/bin/env python3

def greet_programmer():
    pass

def greet(name):
    pass

def greet_with_default(name="programmer"):
    pass

def add(num1, num2):
    pass

def halve(number):
    pass

# <--FUNCTIONS-->

# JS vs. Python
'''
-Use 'def' instead of 'function' keyword for function blocks
-snake_case instead of camelCase
-use colon ':' instead of curly brackets to start code block
-must indent code block to be executed, standard is 4 spaces
-return statements work the same, just no semicolon
-to end code block, new code is written at original indent level
'''


def my_function(param):
    print("Running my_function")
    return param + 1

my_function_returned_value = my_function(1)
print(my_function_returned_value)

my_function_returned_value

'''
-Methods are just functions that belong to objects
-They often act upon those objects when called
'''

# Start on Arguments tomorrow