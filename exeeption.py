"""try:
    number=int(input("enter a number"))
    print("you entered",number)
except ValueError:
    print("error:please enter a valid integer value")    """
try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("error: cannot divide by zero")
except ValueError:
    print("error: please ebter only integers ")