# Prints numbers less than user input from list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
userList= []

for x in a:
    if x <= 5:
        print(x)
        newList.append(x)
    
    
print(newList)

num= int(input("Please enter a number: "))
for y in a:
    if y <= num:
        userList.append(y)

print(userList)

#print( [ x for x in a if x<5 ] )