import subprocess
subprocess.run("clear", shell=True)

# membership operators: in, not in
my_list = [1, 2, 3, 4, 5]
print("Is 3 in the list?", 3 in my_list)  # Output: True
print("Is 6 not in the list?", 6 not in my_list) # Output: True