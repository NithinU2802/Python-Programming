'''

    Exception Handling...

'''

try:
    x=int(input())
    y=x/0
except ZeroDivisionError:
    print("Error: Division by Zero")
except ValueError:
    print("Error: Invalid Input")
