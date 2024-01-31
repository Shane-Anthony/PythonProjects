#Print all the divisors of user input

num = int (input ("Please input a number: "))

listRange = list(range(1, num+1))

divisorList= []

for x in listRange:
    if num % x == 0:  # num must be before x
        divisorList.append(x)

print(divisorList)