

def roman(number=int()):
    value = str(number)
    symbol = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
              10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
              100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
              1000: 'M', 2000: 'MM', 3000: 'MMM'}

    size = len(value)
    result = ''
    if size == 1:
        result = str(symbol[int(value)])

    elif size == 2:
        result = str(symbol[int(value[0]) * 10])
        if int(value[1]) >= 1:
            result += str(symbol[int(value[1])])

    elif size == 3:
        result = str(symbol[int(value[0]) * 100])
        if int(value[1]) >= 1:
            result += str(symbol[int(value[1]) * 10])
        if int(value[2]) >= 1:
            result += str(symbol[int(value[2])])

    elif size == 4:
        result = str(symbol[int(value[0]) * 1000])
        if int(value[1]) >= 1:
            result += str(symbol[int(value[1]) * 100])
        if int(value[2]) >= 1:
            result += str(symbol[int(value[2]) * 10])
        if int(value[3]) >= 1:
            result += str(symbol[int(value[3])])
    return result
