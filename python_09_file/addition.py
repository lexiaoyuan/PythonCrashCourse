while True:
    num1 = input("number 1: ")
    if num1 == 'q':
        break
    num2 = input("number 2: ")
    if num2 == 'q':
        break
    try:
        sum = int(num1) + int(num2)
        print(num1 + " + " + num2 + " = " + str(sum))
    except ValueError:
        print("Value Error！")
