import re


def int_to_roman(int_num):  
    
    int_roman = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 
        90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }
    
    if(int_num in int_roman):
        return int_roman[int_num]
    
    for i in [1000, 100, 10, 1]:
        for j in [9*i, 5*i, 4*i, i]:
            if(int_num >= j):
                return int_to_roman(j) + int_to_roman(int_num-j)


def roman_num_value(roman_num): 
    if (roman_num == 'I'): 
        return 1
    if (roman_num == 'V'): 
        return 5
    if (roman_num == 'X'): 
        return 10
    if (roman_num == 'L'): 
        return 50
    if (roman_num == 'C'): 
        return 100
    if (roman_num == 'D'): 
        return 500
    if (roman_num == 'M'): 
        return 1000
    return -1


def roman_to_int(roman_num):
    result = 0
    index  = 0
  
    while (index  < len(roman_num)):
  
        current_num = roman_num_value(roman_num[index])
  
        if (index + 1 < len(roman_num)): 
            next_num = roman_num_value(roman_num[index + 1]) 
            if (current_num >= next_num): 
                result = result + current_num
                index = index + 1
            else: 
                result = result + next_num - current_num 
                index = index + 2
        else: 
            result = result + current_num 
            index = index + 1

    return result


def sorted_nicely(l):
    """ Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

# names = ['George IV', 'George X', 'William L', 'William X', 'George XI', 'William II', 'Elizabeth I', 'William I',
    # 'Elizabeth VI', 'Elizabeth IV', 'Elizabeth VII', 'Elizabeth VI']

names = ['William V', 'George VI', 'George C', 'William L', 'George V', 'William II', 'George IV', 'Elizabeth I', 'William I']

def sort_names(names):
    
    if len(names) == 0:
        return []
    

    for i in range(0, len(names)):
        roman_num = names[i].split(" ")
        int_num = roman_to_int(roman_num[1])
        names[i] = roman_num[0] +' '+ str(int_num)
    
    print(names)

    sort_names = sorted_nicely(names)
    print(sort_names)

    for i in range(0, len(sort_names)):
        name = sort_names[i].split(" ")
        roman_num = int_to_roman(int(name[1]))
        sort_names[i] = name[0] +' '+ roman_num

    print(sort_names) 

sort_names(names)