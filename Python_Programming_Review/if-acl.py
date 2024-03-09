aclnumber = int(input("What the is IPv4 ACL number? \n"))

if (1 <= aclnumber <= 99) or (1300 <= aclnumber <= 1999):
    print("You are using a IPv4 ACL Standard.")
elif (100 <= aclnumber <= 199) or (2000 <= aclnumber <= 2699):
    print("You are using a IPv4 ACL Extended.")
else:
    print("The IPv4 ACL typed not belong a IPv4 ACL Standard or EXtended.")

