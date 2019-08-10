# def decode(s):
#     if s == "I":
#         return 1
#     elif s == "V":
#         return 5
#     elif s == "X":
#         return 10
#     elif s == "L":
#         return 50

decode = {'I':1, 'V':5, 'X':10, 'L':50}

def romanToInt(num):
    res = 0

    for i in range(0, len(num)-1):
        if decode[num[i]] < decode[num[i+1]]:
            res -= decode[num[i]]
        else:
            res += decode[num[i]]

    res = res + decode[num[len(num) - 1]]
    return res


def getSortedList(names):

    if len(names) == 0:
        return []

    copy_names = [[a,a] for a in names]
    copy_names = sorted(copy_names, key=lambda x:x[0])

    for i in range(0, len(copy_names)):
        n2 = copy_names[i][0].split(" ")
        num = str(romanToInt(n2[1]))
        copy_names[i][0] = n2[0]+ " " + num


    copy_names = sorted(copy_names, key=lambda x:x[1])
    res = [a[1] for a in copy_names]

    return res


# arr = ["Richard V","Henry VI","Edward II","Richard XXV","Henry IX","Edward L"]
# arr = ['William V', 'George VI', 'William L', 'George V', 'William II', 'George IV', 'Elizabeth I', 'William I']
arr = ['George IV', 'George X', 'William L', 'William X', 'George XI', 'William II', 'Elizabeth I', 'William I',
    'Elizabeth VI', 'Elizabeth IV', 'Elizabeth VII', 'Elizabeth VI']

print(getSortedList(arr))