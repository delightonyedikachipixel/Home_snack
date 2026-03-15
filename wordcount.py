sentence = input("Enter a sentence: ")

count = 0

for counter in range(len(sentence)):
    if sentence[counter] == ' ':
        count += 1

count += 1

print(count)
