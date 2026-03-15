def show_menu():
    print("Welcome to Iya Scambirah Pizza Jungle, Ajegunle!!!")
    print("1. Sapa Size    4 slices   ₦2000")
    print("2. Small Money  6 slices   ₦2400")
    print("3. Big Boys     8 slices   ₦3000")
    print("4. Odogwu       12 slices  ₦4200")


def get_guests():
    guests = int(input("Enter number of guests: "))
    return guests


def get_choice():
    choice = int(input("Choose pizza (1-4): "))
    return choice


def get_pizza_details(choice):
    if choice == 1:
        return "Sapa Size", 4, 2000
    elif choice == 2:
        return "Small Money", 6, 2400
    elif choice == 3:
        return "Big Boys", 8, 3000
    elif choice == 4:
        return "Odogwu", 12, 4200
    else:
        return None, 0, 0


def calculate_boxes(guests, slices):
    boxes = guests // slices
    if guests % slices != 0:
        boxes += 1
    leftover = (boxes * slices) - guests
    return boxes, leftover


def print_summary(name, boxes, leftover, total_price):
    print("\nOrder Summary")
    print("-------------------")
    print("Pizza:", name)
    print("Boxes needed:", boxes)
    print("Leftover slices:", leftover)
    print("Total price: ₦", total_price)


def pizza_order():
    show_menu()

    guests = get_guests()
    choice = get_choice()

    name, slices, price = get_pizza_details(choice)

    if name is None:
        print("Pizza not available.")
        return

    boxes, leftover = calculate_boxes(guests, slices)
    total_price = boxes * price

    print_summary(name, boxes, leftover, total_price)


pizza_order()
