var reA = /[^a-zA-Z]/g;
var reN = /[^0-9]/g;

function sortAlphaNum(a, b) {
    var aA = a.replace(reA, "");
    var bA = b.replace(reA, "");
    if (aA === bA) {
        var aN = parseInt(a.replace(reN, ""), 10);
        var bN = parseInt(b.replace(reN, ""), 10);
        return aN === bN ? 0 : aN > bN ? 1 : -1;
    } else {
        return aA > bA ? 1 : -1;
    }
}


function RomantoNumeral(r) {
    let result = 0,
        keys = { M: 1000, D: 500, C: 100, L: 50, C: 100, L: 50, X: 10, V: 5, I: 1 },
        order = Object.keys(keys),
        rom = Array.from(r)

    rom.forEach((e, i) => {
        if (i < rom.length - 1 && order.indexOf(e) > order.indexOf(rom[i + 1])) {
            result -= keys[e]
        } else {
            result += keys[e]
        }
    })
    return result
}

function convertToRoman(num) {
    var roman = {
        M: 1000,
        CM: 900,
        D: 500,
        CD: 400,
        C: 100,
        XC: 90,
        L: 50,
        XL: 40,
        X: 10,
        IX: 9,
        V: 5,
        IV: 4,
        I: 1
    }
    var result = '';
    for (var key in roman) {
        if (num == roman[key]) {
            return result += key;
        }
        var check = num > roman[key];
        if (check) {
            result = result + key.repeat(parseInt(num / roman[key]));
            num = num % roman[key];
        }
    }
    return result;
}

console.log(convertToRoman(36));

// let names = ['Elizabeth 1', 'George 4', 'George 5', 'George 6', 'George 100', 'William 1', 'William 2', 'William 5', 'William 50']
let names = ['William MMMMCMXCIX', 'William V', 'George VI', 'George C', 'William L', 'George V', 'William II', 'George IV', 'Elizabeth I', 'William I']

function sortNames(names) {

    if (names.length == 0)
        return []

    for (let i = 0; i < names.length; i++) {
        let name = names[i].split(' ')
        let int_num = RomantoNumeral(name[1])
        names[i] = name[0] + ' ' + int_num.toString()
    }

    console.log(names)
    names.sort(sortAlphaNum)
    console.log(names)

    for (let i = 0; i < names.length; i++) {
        let name = names[i].split(' ')
        let roman_num = convertToRoman(parseInt(name[1]))
        names[i] = name[0] + ' ' + roman_num
    }
    console.log(names)

}

sortNames(names)
