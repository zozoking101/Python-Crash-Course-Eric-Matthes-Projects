# Python Crash Course By Eric Matthes
# Chapter 8 Ex 8-16
# Imports.py

"""
Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

# Approach 1: Import the entire module
import my_module

my_module.my_function()

# Approach 2: Import a specific function
from my_module import my_function

my_function()

# Approach 3: Import with an alias
from my_module import my_function as fn

fn()

# Approach 4: Import the entire module with an alias
import my_module as mn

mn.my_function()

# Approach 5: Import all functions from the module
from my_module import *

my_function()