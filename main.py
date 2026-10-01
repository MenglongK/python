import cowsay
import random

" Print a cow saying 'Ratana' "
cowsay.cow("Ratana")

" Print the sum of two numbers "
def sum_numbers(a,b):
    return a + b
result = sum_numbers(1,1)
print(f"The sum of 1 and 1 is: {result}")
print("The result of 5 + 10 is:", sum_numbers(5,10))

" Print the name of the user "
" global variable name is defined outside the function and can be accessed inside the function "
name = "Oudom"
def print_name():
    global name
    name = "Ratana"
    print("Local name inside function:", name)
print_name()
print("Global name outside function:", name)

" Print the type of a variable "
name = "Ratana"
number = 5
print(type(name))
print(type(number))

" Print a random number between 1 and 10 "
print("Random number between 1 and 10:", random.randrange(1,10,2))

" loop in string "
for a in "Ratana":
    print(a)
print("The length of the string 'Ratana' is:", len("Ratana"))

" check condition "
text = " Python is funny "
print("fun" in text)  # Output: True
print("Java" in text)  # Output: False
print("Python" not in text)  # Output: False

" Slicing in string "
print("Slicing the string: ", text[0:6])  # Output: Python
print("Slicing the string: ", text[7:])  # Output: is fun

" Modify string "
print(text.upper())  # Output: PYTHON IS FUN

" Remove whitespace from string "
print(text.strip())  # Output: "Python is fun"

" Replace string "
print(text.replace("fun", "awesome"))  # Output: Python is awesome
print(text.replace("n", "N"))  # Output: Python is fuNNy

" Split string "
print(text.split(" ")) # Output: ['Python', 'is', 'fun']

" string concatenation "
print("Hello" + " " + "World")  # Output: Hello World