# Python program to convert Roman Numerals 
# to Numbers 
  
def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1
  
def romanToDecimal(str):
    res = 0
    i = 0
  
    while (i < len(str)):
  
        s1 = value(str[i])
  
        if (i+1 < len(str)): 
            s2 = value(str[i+1]) 
            if (s1 >= s2): 
                res = res + s1
                i = i + 1
            else: 
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
    
    return res

# print("Integer form of Roman Numeral is")
# print(romanToDecimal("XLVII")

inp = ['William V', 'George VI', 'William L', 'George V', 'William II', 'Elizabeth I', 'William I']

def Repeat(inp):
    import pdb; pdb.set_trace()
    _size = len(inp)
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if inp[i] == inp[j] and inp[i] not in repeated: 
                repeated.append(inp[i])
    return repeated

Repeat(inp)