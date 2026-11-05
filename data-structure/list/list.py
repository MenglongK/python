import subprocess

subprocess.run("clear", shell=True)

fruits = ["apple", "cherry", "banana", "orange", "orange"]

# use append to insert item at the last element
print("1. using append: ", fruits)

# use insert to insert item at the specific element
fruits.insert(1, "durian")
print("2. using insert: ", fruits)

# use remove to remove item by name but can be removed only the first item of duplicate items
fruits.remove("orange")
print("3. using remove: ", fruits)

# use pop to remove item by specific index or last item
fruits.pop(1)
print("4. using pop: ", fruits)

# to remove all duplicate item
while 'orange' in fruits:
    fruits.remove("orange")
print("3.1. using while loop to remove all duplicate elements: ", fruits)

# to sort by alphabet
print("5. sort by alphabet: ", sorted(fruits))

# to print length of element
print("6. length of list: ", len(fruits))
