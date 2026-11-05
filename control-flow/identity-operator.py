import subprocess
subprocess.run("clear", shell=True)

# identity operators: is, is not
x = [1, 2, 3]
y = [1, 2, 3]
print("x is y:", x is y)  # Output: False
print("x is not y:", x is not y)  # Output: True
print(id(x), id(y))  # Output: Different memory addresses