word= input("Enter a string: ")
reversed_word = ""
for word_index in range(len(word) - 1, -1, -1):
    reversed_word += word[word_index]
print("Reversed:", reversed_word)
