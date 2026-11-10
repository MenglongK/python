import subprocess

subprocess.run("clear", shell=True)

print("=======================")
print("PRACTICE SHEET: List")
print("=======================")
print("1. Create shopping list containing at least 5 items. Include 'milk' twice")
shopping_list = ["milk", "coca", "pepsi", "fanta", "milk", "sprite"]
print("Shopping list:", shopping_list)

print("\n2. Print the second item, the last item and the total of items")
print("The second item: ", shopping_list[1])
print("The last item: ", shopping_list[-1])
print("The total items: ", len(shopping_list))

print("\n3. Add 'eggs' to the end of the list")
shopping_list.append("eggs")
print("Updated list:", shopping_list)

print("\n4. Remove 'milk' from the list once")
shopping_list.remove("milk")
print("Updated list:", shopping_list)

print("\nWill 'milk' still exist after removing once? ->", 'milk' in shopping_list)
print("Print the number of items remaining:", len(shopping_list), "items")

print("\nUse loop to print each item in separate line & print total number of items")
for item in shopping_list:
    print("Item:", item)
print("Total:", len(shopping_list), "items")

print("\nRemove last item and print updated list")
removed_item = shopping_list.pop()
print("Removed item: ", removed_item)
print("Updated list:", shopping_list)

print("\nSort the final list by alphabetical order and keep the original list")
sorted_list = sorted(shopping_list)
print("Sorted list:", sorted_list)
print("Original list:", shopping_list)

print("\n=======================")
print("PRACTICE SHEET: Tuple")
print("=======================")

print("\nI. STUDENT REGISTRATION")
print("1. Create tuple name of the students")
Student_information = ("dara", 20, "Computer Science", "Year3")
print("Student information:", Student_information)

print("\n2. Print student's name and major")
print("Student's name:", Student_information[0])
print("Student's major:", Student_information[2])

print("\n3. Print total number of items")
print("Total number of items:", len(Student_information))

print("\n4. Print student's year using negative index")
print("Student's year:", Student_information[-1])

print("\nII. COURSE ENROLLMENT")
student_enroll = ("Python", "Database", "Networking", "Python", "Web development")
print("1. Create a tuple course")
print("Student enrollment:", student_enroll)

print("\n2. Count how many time 'Python' appear")
print("Time of 'Python' appear:", student_enroll.count("Python"))

print("\n3. Find the index position of 'Networking'")
print("Index of 'Networking':", student_enroll.index("Networking"))

print("\n4. Use for loop to print each course separately")
for course in student_enroll:
    print("Course:", course)

print("\nIII. UPDATING STUDENT COURSE")
print("\n1. Create a tuple registered_course")
registered_course = ("Python", "Database", "Networking")
print("Registered course:", registered_course)

print("\n2. Convert tuple to list")
tuple_to_list = list(registered_course)
print("Tuple to list:", tuple_to_list)

print("\n3. Add 'Cloud computing' to list")
tuple_to_list.append("Cloud computing")
print("Updated list:", tuple_to_list)

print("\n4. Convert list back to tuple")
list_to_tuple = tuple(tuple_to_list)
print("Tuple to list:", list_to_tuple)
print("\n5. Print updated list")
print("Updated list:", list_to_tuple)

print("\n=======================")
print("PRACTICE SHEET: Set")
print("=======================")

print("\nI: SETUP")
print("1. Create the two sets, yesterday and today, with the files above.")
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}
print("Yesterday:", yesterday)
print("Today:", today)

print("\nII. NEW AND DELETE FILES")
print("1. Find the files that exist today but did not exist yesterday.")
exist_today = today.difference(yesterday)
print("2. Find the files that exist yesterday but are gone today")
exist_yesterday = yesterday.difference(today)
print("\nNew files that exist today:", exist_today)
print("New files that exist yesterday:", exist_yesterday)

print("III. UNCHANGED FILES")
print("1. Find the file that exist on both day")
print("2. Print them")

unchanged_files = today.intersection(yesterday)
print("\nUnchanged files:", unchanged_files)

print("\nIV. ALL CHANGES")
print("1. Find every file that was either added or deleted")
all_changes_file = today.symmetric_difference(yesterday)
print("\nAll changes file:", all_changes_file)

print("\nV. ALL FILES EVER SEEN")
print("1. Build one set containing every file that appear on either day")
print("2. Print it")
all_files_ever_seen = today.union(yesterday)
print("\nAll changes ever seen:", all_files_ever_seen)

print("\n=======================")
print("PRACTICE SHEET: Dictionary")
print("=======================")

print("\n1. Create a dictionary called inventory with 3 products and their stock number")
inventory = {"apple": 5, "banana": 4, "orange": 3}
print("Inventory:", inventory)

print("\n2. Use get() to check the stock of a product that may not exist")
mango_stock = inventory.get("mango", "Not in stock")
print("Stock of mango:", mango_stock)

print("\n3. Use update() to add 2 new products and change one stock number.")
inventory.update({"grape": 4, "melon": 10, "apple": 5})
print("Updated inventory:", inventory)

print("\n4. Use items() to print every product and its stock.")
for product, stock in inventory.items():
    print(f"Product: {product}\nStock: {stock}")

print("\n5. Use pop() to remove a product that is sold out.")
removed_stock = inventory.pop("banana")
print("Removed banana (sold out). Previous stock:", removed_stock)
print("Inventory after pop:", inventory)

print("\n6. Use setdefault() to add a new product only if it is not already there.")
inventory.setdefault("kiwi", 15)
inventory.setdefault("orange", 999)
print("Inventory after setdefault:", inventory)

print("\n7. Use values() and sum() to print the total number of items in stock.")
total_stock = sum(inventory.values())
print("Total items in stock:", total_stock)

print("\n8. Use copy() to save a backup, then clear() the original.")
inventory_backup = inventory.copy()
inventory.clear()
print("Backup inventory:", inventory_backup)
print("Original inventory after clear:", inventory)