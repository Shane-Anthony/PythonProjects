#Evaluate whether a number is odd or even

num= int(input("Please Enter a number: "))

modulo = num % 2
if modulo == 0:
    print ("Even")
elif modulo >= 1:
    print ("Odd")

    