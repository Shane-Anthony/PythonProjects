import random
import string

print (" \n Welcome to the Password Generator! \n")

length = int(input("How many characters long do you require your password to be? "))

print('''Please pick which Character sets will make up your Password: \n
      1. Numbers 
      2. Letters
      3. Special characters
      4. Exit ''')

set= ''

while (True):
    setChoice = input("Please pick a Character Set: ")
    if (setChoice == '1'):
        set += string.digits
    elif (setChoice == '2'):
        set += string.ascii_letters
    elif (setChoice == '3'):
        set += string.punctuation
    elif (setChoice == '4'):
        break
    else:
        print ("Please try again.")

password = []

for x in range(length):
    char = random.choice(set)

    password.append(char)

print("".join(password))