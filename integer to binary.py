a = 9
result = ""
result1 = ""
while a > 0:
    a = a // 2
    if a % 2 != 0:
        result += "1"
    else:
        result += "0"

    result1 += str(a)

print(result, result1)
