try:
    a=int(input("gimme a number"))
    c=1/a
    print(c)
except ValueError as e:
    print("enter a valid value")

except ZeroDivisionError as e:
    print("make sure you are not dividing it by zero")

print("thnxx for using this code!")