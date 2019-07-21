

x = input('Enter a number: ')

def fact(x):

    if x > 1:
        return x * fact(x-1)
    elif x < 0:
        return (x * fact(x+1))
    else:
        return 1

f = fact(int(x))
print(f)