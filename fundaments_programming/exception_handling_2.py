try:
    a = 1/0
except ZeroDivisionError as ex:
    print("cannot divide by Zero, ZeroDivisionError, ", ex)
finally:
    print("done")


try: 
    y = a + 5
except NameError as exp:
    print("Exception occured:", exp)
finally:
    print("in finally")

try: 
    a = [1,2,3]
    print(a[10])
except IndexError as exp:
    print("exp:", exp)
finally:
    print("in finally")


try:
    a = 10
    b = int(input("Please input a number to divide a = "))
    a = a/b
    print(f"Suscces:a={a}")
except ZeroDivisionError as exp:
        print("exp:", exp)
except ValueError as ve:
    print("exception:", ve)
finally:
    print("in finally")