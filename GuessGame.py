import random

num= random.randint(1,9)

print(num)

userNum = 0
guesses = 0

while userNum != num and userNum != "exit":
    guesses +=1
    try:
        
        userNum = input ("Enter a number between 1-9: ")
        if userNum == "exit":
            break
        userNum = int(userNum)
        if userNum < num:
            print ("Too Low. ")
        elif userNum > num:
            print ("Too High. ")
        elif userNum == num:
            print("Correct, Well Done!")
            print ("Number of wrong guesses: "+ str(guesses))
        elif userNum == "exit":
            break
    except ValueError:
        print("Please try again.")
    
  

    
