def OddOrEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
input_num = int(input("Enter a number: "))
print(OddOrEven(input_num))