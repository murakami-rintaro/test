for i in range(1, 31):
    flag1 = i % 3 == 0
    flag2 = i % 5 == 0
    if flag1 and flag2:
        print("FizzBuzz")
    elif flag1:
        print("Fizz")
    elif flag2:
        print("Buzz")
    else:
        print(i)