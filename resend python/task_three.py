number = int(input("Enter a number: "))

count = 0  

while number != 1:

    if number % 2 == 0:
        number = number // 2
        print("Divided by 2:", number)
    else:
        number = (number // 3) + 1
        print("Divided by 3 + 1:", number)

    count += 1  

print("Total number of divisions:", count)
