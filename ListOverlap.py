#Create 2 random lists and print the elements that are common between both

import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,89]

a=(random.sample(range(1,10),5))
b=(random.sample(range(1,10),7))




print ("List A: ", a)
print ("List B: ", b)

duplicate = []

for x in a:
    for y in b:
        if x == y:
            duplicate.append(x)

duplicate.sort()
print("Common Elements between Lists:", duplicate)