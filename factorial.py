


def factorial(inputValue):
    if inputValue==0:
        return inputValue
    elif inputValue==1:
        return inputValue
    else:
        return inputValue*factorial(inputValue-1)

Number = 6
print("factorial of number")
print(factorial(Number))
