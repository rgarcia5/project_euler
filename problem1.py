def multiples():
    num = 999
    result = 0
    while (num > 0):
        if (num % 5 == 0 or num % 3 == 0):
            result += num
        num -= 1
    return result


print multiples()
