from contextlib import nullcontext


def two_fer(name):
    if name == nullcontext:
        return ('One for you, one for me.')
    else:
        return('One for' + " " + str(name) + ", " + 'one for me.')

print(two_fer())