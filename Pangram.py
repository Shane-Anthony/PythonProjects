text= input("Enter a Pangram: ")

def pangram(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in text.lower():
            return False
    return True
        
result= pangram(text)

print(result)