number = int(input("enter any number "))
original = number
reverse = 0
print("Original number is",original)
while(number>0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")
