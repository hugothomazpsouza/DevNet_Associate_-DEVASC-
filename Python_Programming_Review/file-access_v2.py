devices = []
file = open("devices.txt", "r")

for item in file:
    item = item.strip() #Strip method to remove whitespaces
    devices.append(item) 

file.close()

print(devices)
