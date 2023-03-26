"""
==============================================
Quiz - Solved in the video
Exercise - Next video
Project - Some awesome python utility
=============================================
"""

# ========Comments and printing======== #

print("Hello World\n","It's my first program")
print("Hello World\nIt's my first \t program")
# single line comment
print("C:\\nimbu")

# ===============Variables============= #
var1="Hello World"
var2="89"
var3="36"
var4="I'm Python"

print(type(var1))
print(var1+var4)

str()
int()
float()

print(10 * str(int(var2)) + str(int(var3)))
print(100 * "Hello Python\n")

# =============User Input============= #
print("Enter your number")
num = input()
print("Your number: ", int(num))
print("Addition of two numbers")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("The Sum of these two numbers are: ", a+b)

# ===========String function========== #
stm="Yash is a best boy"
print(stm[-4:])
print(len(stm))
print(stm.endswith("boy"))
print(stm.count("o"))
print(stm.capitalize())
print(stm.upper())
print(stm.lower())
print(stm.replace("is","are"))

# ===============Lists=============== #
grocery= ["Harpic","vim bar","deodrant"]
print(grocery[:4])
numbers = [2,7,9,11,3]
numbers.sort()
numbers.reverse()
numbers.append(9)
print(numbers)
# use -1 in [::-1]
# Mutable - can change 
# Immutable - cannot change 

# Touple
# Touple is immutable
# (1,) too
tp = (1,2,3)

# Exchange Traditionally
a = 1
b = 8
temp = a
a=b
b = temp
print(a,b)
a,b = b,a
print(a,b)

# =============Dictionary=============== #
dict1 = {"Rajni":"Update",
        "Lawliet":"Global",
        "Noha":{"bf":"rusk",
                "lunch":"roti",
                "dinner":"milk"}}

dict1["Ankit"] = "Junk food"
print(dict1["Noha"]["bf"])
print(dict1)
del dict1["Ankit"]
print(dict)
dict2 = dict1.copy()
del dict2["Rajni"]
dict1.update({"Leena":"Toffee"})
print(dict1.keys())
print(dict1.items())
print(dict1["Noha"].items())

# ================Sets============== #
s = set()
print(type(s))
s_from_list = set([1,2,3.4])
print(s_from_list)
print(type(s_from_list))

p = set()
p.add(1)
p.add(2)
p1 = p.union({1,2, 3})
p2 = p.intersection({1,2, 3})
p3 = {4, 6}
p4 = p.remove(2)
print(p, p1, p2, p.isdisjoint(p3), p4)

# ==========if, elif & else========== #
var = 6
var2 = 56
var3 = int(input("Enter Number to check it's greater or smaller : "))

if var3 > var2:
        print("Greater")

elif var3 == var2:
        print("Equal")
else:
        print("Lesser")

list1 = [1,2,3,4,5]
if 5 in list1:
        print("Yes it's in the list")
print(5 in list1) # True
print(15 in list1) # False
if 15 not in list1:
        print("No, it's not in the list")

print("Enter your age: ")
user_age = int(input())

if 100 < user_age:
        print("You can't have age more then 100")
elif user_age > 18:
        print("OK, You can drive")
elif user_age == 18:
        print("Sorry, we have to manually confirm it that you can drive")
elif user_age < 7:
        print("Sorry, that's not legal age")
else:
        print("No, You can't drive")

# ========Exercise 2 - Faulty Calculator======= #
print("Welcome to Faulty Calculator")
print("First enter any two number and then the operator")
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
operator = str(input("Enter the operator (+,-,*,%,**,//,/) : "))
answer = num1,operator,num2

if num1==45 and num2==3 and operator=="*":
        print("555")
elif num1==56 and num2==9 and operator=="+":
        print("77")
elif num1==56 and num2==6 and operator=="/":
        print("4")
elif operator=="+":
    print("The answer is", num1+num2)
elif operator=="-":
    print("The answer is", num1-num2)
elif operator=="*":
    print("The answer is", num1*num2)
elif operator=="/":
    print("The answer is", num1/num2)
elif operator=="**":
    print("The answer is", num1**num2)
elif operator=="//":
    print("The answer is", num1//num2)
elif operator=="%":
    print("The answer is", num1%num2)
else:
    print("Please enter operator from the given choices only.")

# ================Python Loops=============== #
list1 = [["Harry", 3], ["Larry", 7], ["Carry", 9], ["Marie", 4]]


dict1 = dict(list1)
for boy,lolli in dict1.items():
        print(boy, "ate", lolli, "lollipops.")

# ====================QUIZ======================== #
print("Edit the list then re-run the code\nThis code will tell that list item contain integer or not.\n\nEnter 'yes' or 'no' to continue:")
linum = [1, 2, 3, 'Ok', 5, 6]

agree_int = str(input())
if agree_int == 'yes':
        print('Result:\n')
        for nums in linum:
                if nums == int():
                        a = 'true'
                else:
                        a = 'false'
                if a == 'true':
                        print('Yes', nums, ' is an integer.')
                elif a == 'false':
                        print('No,', nums,' is not an integer.')
elif agree_int == 'no':
        print('Exiting program !')
else:
        print("wrong input. You have to enter 'yes' or 'no' only...")

# correction 
items = [int, float, "Harry", 3, 3, 5, 9, 90, 64]
for item in items:
        if str(item).isnumeric() and item>6:
                print(item," is an integer")




# import time


# print('Open the MyLearning.py file by an IDE.')
# time.sleep(10)
