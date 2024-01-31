import random

a = random.sample(range(1,20),12)
b = random.sample(range(1,20),16)

result = [x for x in a if x in b]
print(a)
print(b)
print(result)