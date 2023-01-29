import numpy as np

binary_string = '010000000111111010111001'

binary_string = binary_string +'0'*(64-len(binary_string))

def createMantisa(binary):
    return sum(int(digit)*2**(-1*(index+1)) for index, digit in enumerate(binary))

def questionOne(binary):
    sign = int(binary[0])
    exponent = int(binary[1:12], 2) - 1023
    mantisa = createMantisa(binary[12:])
    return (-1)**sign * 2**exponent * (1+mantisa)

def findDecimalPoint(string):
    return string.find('.') if '.' in string else -1

#3 digit chopping arithmetic 
def questionTwo(num, decimal_places):
    decimal_index = findDecimalPoint(str(num))
    if decimal_index != -1:
        factor = 10**(decimal_places - decimal_index)
        return int(num * factor) / factor
    else:
        return num
#3 digit rounding arithmetic 
def questionThree(num, decimal_places):
    decimal_index = findDecimalPoint(str(num))
    if decimal_index != -1:
        factor = 10**(decimal_places - decimal_index)
        return int(num * factor + 0.5) / factor
    else:
        return num

#Absolute error
def questionFour(trueVal, approxVal):
    return abs(trueVal - approxVal)

#Relative error
def questionFourPt2(trueVal, approxVal):
    return abs(trueVal - approxVal) / trueVal

#Minimum number of terms needed to computer f(1) with error < 10-4
def questionFive(k: int, x: int, tolerance: float):
    func = "(-1**k) * (x**k) / (k**3)"
    if "(-1**k) * " in func:
        func = func.replace("(-1**k) * ", "")

    if "/ (k**" in func:
        temp = func
        kExp = temp[temp.rindex("**") + 2]
        remPort = "/ (k**" + kExp + ")"
        func = func.replace(remPort, "* k")
        decToExp = (len(str(tolerance).replace("0.",""))) / float(kExp)
        tolerance = 10 ** decToExp

    if x == 1:
        func = func.replace("(x**k) * ","")

    if func == "k":
        tolerance -= 1

    iteration_counter = round(tolerance)
    return iteration_counter

iteration_counter = questionFive(k=1, x=1, tolerance=10 ** (-4))

#Bisection Method
def questionSix(start, end, precision):
    iteration = 0
    def func(x): return x**3 + 4*x**2 - 10
    midpoint = (start + end) / 2
    while abs(start - end) > precision:
        iteration += 1
        if (func(start) < 0 and func(midpoint) > 0) or (func(start) > 0 and func(midpoint) < 0):
            end = midpoint
        else:
            start = midpoint
        midpoint = (start + end) / 2
    return iteration

#Newtonian Method
def questionSixPt2(initial_value: float, precision: float) -> int:
    iteration_count = 0

    def function(x: float) -> float:
        return x**3 + 4*x**2 - 10

    def derivative(x: float) -> float:
        return 3*x**2 + 8*x

    while abs(function(initial_value)/derivative(initial_value)) >= precision:
        initial_value -= function(initial_value)/derivative(initial_value)
        iteration_count += 1

    return iteration_count+1


val = questionOne(binary_string)
print(val)
print()
print(questionTwo(val, 3))
print()
approx = questionThree(val, 3)
print(approx)
print()
print(questionFour(val, approx))
print(questionFourPt2(val, approx))
print()
print(iteration_counter)
print()
print(questionSix(-4, 7, 10**(-4)))
print()
print(questionSixPt2(7, 10**(-4)))