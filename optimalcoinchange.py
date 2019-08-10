def return_change(to_return, coins = [1,2,3,4]):
    flag = None
    for c in coins:
        if c == to_return:  return c
        if c < to_return:
            flag = c
    temp_balance = round(to_return - flag, 2)
    return [flag] + [return_change(temp_balance)]
    
            
result = return_change(8) # Highly nested iterable
print(result)


# Recursive function to flatten an iterable with arbitrary levels of nesting.
# https://stackoverflow.com/a/14491059/3182843
def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item