# Python Variables
# ---------------------------------------------- #
# Variable Declaration and Types
# Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.
# In python, the programmer does not need to declare the variable type explicitly, we just need to assign the value to the variable.
# Example:
name = "Abhishek"   #type str
age = 20            #type int
passed = True       #type bool
obj = [ 2, "Chal Nikal" ] #type array

print(obj[0], obj[1])

# ---------------------------------------------- #
# Valid and Invalid Variable Declaration
Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name

# 5color = "green"    #invalid variable name
# $color = "orange"   #invalid variable name

# ---------------------------------------------- #
# Variable Declaration Case
# Sometimes, a multi-word variable name can be difficult to read by the reader. To make it more readable, the programmer can do the following:
# Example:
NameOfCity = "Mumbai"       #Pascal case
nameOfCity = "Berlin"       #Camel case
name_of_city = "Moscow"     #snake case

# ---------------------------------------------- #
# Scope of variable:
# The scope of the variable is the area within which the variable has been created. Based on this a variable can either have a local scope or a global scope.

# Local Variable:
# A local variable is created within a function and can be only used inside that function. Such a variable has a local scope.
# Example:
icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")
foods()

# Global Variable:
# A global variable is created in the main body of the code and can be used anywhere within the code. Such a variable has a global scope.
# Example:
icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global variable value.") # Prints Global Variable
# print(fruit + " is a local variable value.") # Won'tprint Local Variable