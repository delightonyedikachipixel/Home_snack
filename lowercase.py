text = input("Enter a string: ")

lowercase_counter = 0


for character in text:
    if 'a' <= character <= 'z':  
        lowercase_counter += 1

print("Number of lowercase letters:", lowercase_counter)
