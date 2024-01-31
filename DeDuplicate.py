
def dedupe(i):
    y=[]
    for x in i:
        if x not in y:
            y.append(x)
    return y

a= [1,1,3,4,5,5,6,7,7,7,8]
b= [22,22,44,44]

print(dedupe(a))
