def get_num():
    return (input("Pick a number: "))

num = int(get_num())
listRange = list(range(2, int(num/2)+1))

def check_prime(num):
    for x in listRange:
        if num % x == 0:
            return(str(num)+" is not a Prime Number")
        else:
            return (str(num)+" is a Prime Number")
        
print(check_prime(num))




