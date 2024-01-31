def genFib():
    count = int(input("How many Fibonacci numbers would you like? "))

    x = 1
    
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while x < (count -1):
            fib.append(fib[x] + fib[x-1])
            x += 1
        return fib
    
print(genFib())
