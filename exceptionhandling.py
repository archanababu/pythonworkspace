#------------------------------
# Exception handling
#------------------------------

try:
    n = 100/0
    num1 = int(input("Enter a number : "))
    print(num1)
except ValueError:
    print("Invalid value")
except ZeroDivisionError as er:
    print("Exception catched for divide by zero")
    print(er)