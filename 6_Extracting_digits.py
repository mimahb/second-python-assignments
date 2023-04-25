def reverse(number):
    while(number > 0):
        digit = number % 10
        number = number // 10
        print(digit, end=" ")

number = 7536
reverse(number)