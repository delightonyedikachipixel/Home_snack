print("Welcome to Iya Scambirah Pizza Jungle, Ajegunle!!!")
print("1. Sapa Size    4 slices   ₦2000")
print("2. Small Money  6 slices    ₦2400")
print("3. Big Boys     8 slices     ₦3000")
print("4. Odogwu       12 slices     ₦4200")

guests = input("Enter number of guests: ")

if not guests.isdigit():
    print("Invalid input.")
    

guests = int(guests)

choice = input("Choose pizza (1-4): ")

if not choice.isdigit():
    print("Invalid choice.")
    

choice = int(choice)

if choice == 1:
    slices = 4
    price = 2000
    name = "Sapa Size"
elif choice == 2:
    slices = 6
    price = 2400
    name = "Small Money"
elif choice == 3:
    slices = 8
    price = 3000
    name = "Big Boys"
elif choice == 4:
    slices = 12
    price = 4200
    name = "Odogwu"
else:
    print("Pizza not available.")
    

boxes = guests // slices
if guests % slices != 0:
    boxes = boxes + 1

leftover = (boxes * slices) - guests
total_price = boxes * price

print("\nOrder Summary")
print("-------------------")
print("Pizza:", name)
print("Boxes needed:", boxes)
print("Leftover slices:", leftover)
print("Total price: ₦", total_price)

