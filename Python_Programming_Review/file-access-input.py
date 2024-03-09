
file = open("devices.txt", "a")

while True:
    add_device = input("Do you want to add move devices in the devices list? \n")
    if add_device.lower() == 'yes':
        newitem = input("Enter device name: ")
        file.write(newitem + "\n") 
    else:
        print("All done!")
        break

file.close()
