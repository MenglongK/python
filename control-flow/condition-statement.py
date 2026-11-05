import subprocess
subprocess.run("clear", shell=True)

# condition statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# ternary operator
y = 20
result = "y is greater than 15" if y > 15 else "y is less than or equal to 15"
print(result)