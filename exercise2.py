num = int(input('Type a number:'))
rem = num % 2
if num == 0:
    print(num, 'cannot be even or odd')
else: 
    rem = num % 2
    if rem == 0:
        print(num, 'is an even number.')
    else:
        print(num, 'is an odd number.')
    