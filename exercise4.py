pick = int(input('Please choose a number to divide:'))
list = range(1, pick+1)
divisors = []
for i in list:
    if pick % i == 0:
        divisors.append(i)
    
print('The factors of', pick, 'are', divisors)