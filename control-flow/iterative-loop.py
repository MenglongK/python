import subprocess
subprocess.run("clear", shell=True)

# for loop
print("======for loop======")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit:",fruit)

# for loop with range
print("\n======for loop with range======")
for i in range(5, 10, 2):
    print("i:",i)

# while loop
print("\n======while loop======")
count = 5
while count > 0:
    print("count:",count)
    count -= 1

# while loop with condition
print("\n======while loop with condition======")
option = ""
while option !=4:
    option = int(input("Enter a number (1-4): "))
    if option == 1:
        print("You selected option 1")
    elif option == 2:
        print("You selected option 2")
    elif option == 3:
        print("You selected option 3")
    else :
        print("Exiting the loop")    