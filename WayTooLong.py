num = int(input("How many letters are too many letters? "))

def wordCount(word):
    if len(word) < num:
        print(word.capitalize())
    elif len(word) >= num:
        print(word[0].capitalize()+str(len(word)-2)+ word[-1])
    
print("Write a word and see to see if it is over the characters set. \n Type 'exit' to quit.")

while(True):
    userWord = input("Please input a word: ").lower()
    if userWord == 'exit':
        break
    wordCount(userWord)