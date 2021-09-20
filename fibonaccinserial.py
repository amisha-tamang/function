


def fibonacciSerial(inputValue):
    if inputValue<=1:
        return inputValue
    else:
        return (fibonacciSerial(inputValue - 1)) + fibonacciSerial(inputValue-2)

inputValue = 6
for i in range(inputValue):
    print(fibonacciSerial(i))


