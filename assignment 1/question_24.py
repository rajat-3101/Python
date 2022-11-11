#Write a code to take 3 numbers as an input from the user and display the greatest no as output.

x, y, z = input("Enter three numbers: ").split()

if x>y:
    if x>z:
        print("x is the greatest number")
    else:
        print("z is greatest")
else:
    if y>z:
        print("y is greatest")
    else:
        print("z is greatest")