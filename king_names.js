function decode(s){
    if (s == "I")
        return 1
    else if (s == "V")
        return 5
    else if (s == "X")
        return 10
    else if (s == "L")
        return 50
}

function romanToInt(num){
    let res = 0

    for(let i=0; i<num.length-1; i++){
        if (decode(num[i]) < deode(num[i+1]))
            res -= decode(num[i])
        else { 
            res += decode(num[i])
        }
    }
    res = res + decode(num[num.length - 1])
    return res    
}

def getSortedList(names):

    if len(names) == 0:
        return []

    copy_names = [[a,a] for a in names]
    copy_names = sorted(copy_names, key=lambda x:x[0])

    for i in range(0, len(copy_names)):
        n2 = copy_names[i][0].split(" ")
        num = str(romanToInt(n2[1]))
        copy_names[i][0] = n2[0]+ " " + num


    copy_names = sorted(copy_names, key=lambda x:x[0])
    res = [a[1] for a in copy_names]

    return res


let arr = ['William V', 'George VI', 'William L', 'George V', 'William II', 'Elizabeth I', 'William I']
console.log(getSortedList(arr))

function getSortedList(names){
    if (names.length == 0){
        return []
    }

    let copy_names = [for (a of names) [a, a]];

    let copy_names = sorted(copy_names, key=lambda x:x[0])

    copy_names.sort(([a], [b]) => a.localeCompare(b))

    for i in range(0, len(copy_names)):
        n2 = copy_names[i][0].split(" ")
        num = str(romanToInt(n2[1]))
        copy_names[i][0] = n2[0]+ " " + num


    copy_names = sorted(copy_names, key=lambda x:x[0])
    res = [a[1] for a in copy_names]

    return res
}