
#----------------
# If statement
#----------------

gender = input("Enter your gender (m/f): ")

if gender == 'm'or gender == 'M':
    print("You are a male")
elif gender == 'f'or gender == 'F': 
    print("You are a female")
elif gender != "":
    print("We are unable to identify your gender")
else:
    print("please specify your gender")

#----------------------------
# If statement and comparison
#----------------------------

def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3

print(maxnum(35,23,65))

#-----------------------
# Using simple calculator
#-----------------------

def calc(n1,op,n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '%':
        return n1 % n2
    else:
        return print("Invalid operator")

num1 = float(input("Enter first number : "))
op = input("Enter an operator : ")
num2 = float(input("Enter second number : "))

print(calc(num1,op,num2))
        
