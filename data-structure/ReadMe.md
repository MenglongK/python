## DATA STRUCTURE

**1. List**
```python
fruits = ["apple", "cherry", "banana", "orange"]

# use append to insert item at the last element
fruits.append("orange")
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
```
**2. Tuple (practice)**
```python
print("I. STUDENT REGISTRATION")
print("1. Create tuple name")
student = ("Dara", 20, "Computer Science", "Year 3")
print(student)
print("\n2. Print student name & major")
print("Student name: ", student[0], "\nMajor: ", student[2])
print("\n3. Print total number of items")
print("Total number of items: ", len(student))
print("\n4. Print student year using negative index")
print("Student year: ", student[-1])

print("\nII. COURSE ENROLLMENT")
print("1. Create tuple name")
course = ("Python", "Database", "Networking", "Python", "Web Development")
print(course)
print("\n2. Count how many times Python appear")
print("How many times Python appears: ", course.count("Python"))
print("\n3. Find index position of Networking")
print("Networking index: ", course.index("Networking"))
print("\n4. Using a loop to print each course separately")
for course in course:
    print("Course: ", course)

print("\nIII. UPDATING STUDENT COURSE")
print("1. Create a tuple name of register_course")
register_course = ("Python", "Database", "Networking")
print(register_course)
print("\n2. Convert tuple to list")
new_list = list(register_course)
print(new_list)
print("\n3. Add Cloud computing to the list")
new_list.append("Cloud computing")
print(new_list)
print("\n4. Convert list to tuple")
new_tuple = tuple(new_list)
print(new_tuple)
```
**Dictionary**
```python
user_response = {
    "name": "Menglong",
    "age": 20,
    "Country": "Cambodia"
}

# To print value of "key"
print(user_response.get("Country"))
# To print all key
print(user_response.keys())
# To print all value
print(user_response.values())
# When don't have "key" it will show => Phone not provided
print(user_response.get("Phone", "Phone not provided"))
# To print key pair
print(user_response.items())
# To print each key pair
for key, value in user_response.items():
    print(key, ":", value)

# To update the key pair
change = {
    "theme": "dark",
    "notification": True
}
user_response.update(change)
print("new_user_response:", user_response)

# To clear everything in dictionary
user_response.clear()
print("user_response:", user_response)

# To create empty dictionary
order = {}
print("order:", order)

# To update item into dictionary
order.update({
    "name": "Coca",
    "print": 1
})
print("order:", order)

# To remove last item in dictionary
remove_item = order.popitem()
print("remove_item:", remove_item)  # type tuple
print("order:", order)

player = {"Dara", "Menglong", "Piseth"}
update = dict.fromkeys(player, 0)
print("update:", update)
update.update({"Menglong": 6})
print("update:", update)
```