def FizzBuzz(num):
    if num == 0:
        return 0
    elif (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num

for i in range(100):
    print(FizzBuzz(i+1))
