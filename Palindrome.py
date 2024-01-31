# Checks whether a word is the same reversed

word = input("Please enter a word: ").lower()

reverse = word[::-1]
print (reverse)

if reverse == word:
    print(word.capitalize(), "is a Palindrome")
else:
    print(word.capitalize(), "is not a Palindrome")