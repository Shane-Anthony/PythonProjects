import sys

name=input("What is your name, friend? ")
age=int(input("How old are you exactly, " + name + "? "))

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

ageBy100 = 2024 + 100 - age
years = 100 - age

bday = input("Have you had your birthday yet this year? ").lower()
if bday in yes:
   bday = True
elif bday in no:
   bday= False
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
   sys.exit(1)

if bday == False:
   ageBy100 -= 1
   years -=1

   


print ("So if my calculations are correct " + name +". You are " + str(age) + " years old, which means you will be 100 in the year " + str(ageBy100) + ". This is in " + str(years) + " years.")
