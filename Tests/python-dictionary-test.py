

dict = {
        "Integer":"""An Integer
(from the Latin integer meaning "whole")
is colloquially defined as a number
that can be written without a fractional component.""",

        "String":"""A string in Python is a sequence of characters.
It is a derived data type. Strings are immutable. 
This means that once defined,
they cannot be changed.""",

        "Float":"""The Python float() method converts a number stored in a string
or integer into a floating point number,
or a number with a decimal point.""",

        "Dictionary":"""Dictionaries are Python's implementation of a
data structure that is more generally known as an associative array.
A dictionary consists of a collection of key-value pairs.
Each key-value pair maps the key to its associated value.""",

        "Variable":"""A Python variable is a reserved memory location to store values.
In other words, a variable in a python program gives data to the computer for processing.""",

        "Python":"""Python is an open source programming language,
that was made to be easy-to-read and powerful.
A Dutch programmer named Guido van Rossum made Python in 1991.
He named it after the television show Monty Python's Flying Circus...
This means that a programmer can change the code
and quickly see the results."""
        }


print("Please only ask the meaning of following words below 😅😅\n Integer, Float, String, Dictionary, Python, Variable.")
print("Enter any one word:")
word = str(input())

means = dict[word]

print(means)


























