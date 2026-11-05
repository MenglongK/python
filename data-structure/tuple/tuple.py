import subprocess
subprocess.call("clear", shell=True)

fruits = ("apple", "banana", "cherry")

# convert tuple to list for reassign the value due tuple is immutable
new_list = list(fruits)
new_list[0] = "banana"
print("printing fruits: ", new_list)

# convert list to tuple
new_tuple = tuple(new_list)
print("printing tuple: ", new_tuple)