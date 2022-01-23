phrase = input('Type a word or phrase to check if it is a palidrome:')


def change(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace('.', '')
    phrase = phrase.replace(' ', '')
    return phrase


backwards = change(phrase)[len(phrase)-1:0:-1]
full_back = backwards + backwards[0]

if change(phrase) == change(full_back):
    print(phrase.capitalize(), 'is a palindrome.')
    
else:
    print(phrase.capitalize(), 'is not a palidrome.')

    
    