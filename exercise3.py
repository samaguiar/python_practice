ask = input('Enter a number or Press Q to quit:')
user_list = []
list_under_5 = []
while ask != 'Q':
    ask = int(ask)
    user_list.append(ask)
    ask = input('Enter a number or Press Q to quit:')
else:
    for i in user_list:
        if i < 5:
            list_under_5.append(i)
print('The numbers under 5 in your list are:', list_under_5)

