file = open("devices.txt", "r")

for item in file:
    item = item.strip() #Strip method to remove whitespaces
    print(item)

file.close()
