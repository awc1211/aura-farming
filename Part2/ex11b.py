def calculate(number1, operator1, number2):
    if operator1 == '+' :
        return number1 + number2
    elif operator1 == '-':
        return number1 - number2
    elif operator1 == '*':
        return number1 * number2
    elif operator1 == '/':
        if number2 == 0:
            return "Cannot divide by zero"
        else:
             return number1 / number2
    else:
        return "Invalid operator"
    

print(calculate(5, '+', 2))
print(calculate(5, '-', 2))
print(calculate(5, '*', 2))
print(calculate(5, '/', 2))
print(calculate(5, '/', 0))
print(calculate(5, '>', 2))