try:
    answer = 10/0
    vale = int(input("enter a number : "))
except ZeroDivisionError as err:
    print(err)
except ValueError as val:
    print(val)