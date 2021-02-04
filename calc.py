def add(num1, num2): 
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    return num1 + num2

def subtract(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    return num1 - num2

def multipy(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    return num1 * num2

def divide(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
         return "Error"
    if num2 == 0:
        return "Error"
    else:
       return num1 / num2 

subtract(10, "yes")