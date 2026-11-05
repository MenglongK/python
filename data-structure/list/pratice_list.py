import subprocess

subprocess.call("clear", shell=True)

shop = ["milk", "milk", "coffee", "apple", "banana"]

print("1. The second item is: ", shop[1])
print("2. The last item is: ", shop[-1])
print("3. Total number of items: ", len(shop))
shop.append("egg")
print("4. Add egg to end of list: ", shop)
shop.insert(1, "bread")
print("5. Insert bread to the second item: ", shop)
shop.remove("milk")
print("6. Remove milk from the list: ", shop)
print("7. Total number of items: ", len(shop))

for item in shop:
    print("Item: ", item)

print("8. Total number of items: ", len(shop))

remove_item = shop.pop()
print("9. Remove last item from the list: ", remove_item)

print("10. Sort the list: ", sorted(shop))
print("10.1. the original list: ", shop)