import random

a = random.sample(range(0,100), 10)
b = random.sample(range(0,100), 10)
c = []

for i in a: 
    if i in b:
        c.append(i)

print('List a contains:', a)
print('List b contains:', b)
print('The numbers lists a and b have in common are:', c)
