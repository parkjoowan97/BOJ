roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
numbers =  [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def roman_to_arabic(string):
    total = 0
    prev_value = 0
    for char in reversed(string):
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

def arabic_to_roman(number):
    result = ''
    for value, numeral in numbers:
        while number >= value:
            result += numeral
            number -= value
    return result

T = int(input())
for _ in range (0,T):
    A = input()
    try:
        A = int(A)
    except:
        answer = roman_to_arabic(A)
    else:
        answer = arabic_to_roman(A)
    print(answer)