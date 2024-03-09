while True:
    x = input("Enter a number to count to: ")
    if (x == 'q') or (x == 'quit'):
        break

    x = int(x)
    y = 1

    while y<=x:
        print(y)
        y += 1
