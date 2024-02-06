import re

print( "Welcome to Decapitalize. If you have a bunch of text you need to make lowercase, we can help! \n ")

text= input('Enter Your Text: ')

def Decapitalize(exText):
    exText = exText.lower()
    return(exText)

decap = Decapitalize(text)

print('Decapitalised text: ',decap)



def capitalize(exText):
    cap = input("Would you like this capitalised after fullstops? Yes/No: \n").lower()
    if cap in {'yes','y','ye'}:
        exText = re.split('(?<=[.!?]) +',exText)
        exText = [sentence.capitalize() for sentence in exText]
        exText = ' '.join(exText)
        return(exText)
    elif cap in {'no','n','nah'}:

        return (exText)
    else:
        print("\nInvalid Response! Please try again. ")
        return(exText)


recap = capitalize(decap)
print("Your final text: \n", recap, '\n')

print ("Thanks for using DeCapitalize! Goodbye. \n")