def reverse_number(number):
    result = 0
    while number > 0:
        temp = number % 10
        result = result * 10 + temp
        number //= 10

    return result


print(reverse_number(193))
