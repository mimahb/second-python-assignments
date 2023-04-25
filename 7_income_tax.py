income = [4500]
for i in income:
    if i <= 10_000:
        tax = (10_000 * 0) + (10_000 * 10) + (i * 20)
        print("your tax is: ",tax)

    else:
        print("your tax is 0")