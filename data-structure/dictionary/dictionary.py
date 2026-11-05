import subprocess

subprocess.call("clear", shell=True)

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
