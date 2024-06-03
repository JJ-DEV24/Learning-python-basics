"""Calculator"""



def calculator():
    first_number = int(input("Hello. Please enter your first number: "))
    ope = input("Please choose an operator: ")
    second_number = int(input("Please enter your second number: "))
    answer = operator(ope, first_number, second_number)
    print(answer)


def operator(a_operator: str, first_number, second_number):
    ans = 0
    if a_operator == '+':
        ans = add(first_number, second_number)

    elif a_operator == '-':
        ans = subtract(first_number, second_number)

    elif a_operator == '*':
        ans = multiply(first_number, second_number)

    elif a_operator == '/':
        ans = divide(first_number, second_number)
    return ans


def add(first_number: int | float, second_number: int | float) -> int | float:
    answer: int | float = first_number + second_number
    return round(answer, 2)


def subtract(first_number: int | float, second_number: int | float) -> int | float:
    answer: int | float = first_number - second_number
    return round(answer, 2)


def multiply(first_number: int | float, second_number: int | float) -> int | float:
    answer: int | float = first_number * second_number
    return round(answer, 2)


def divide(first_number: int | float, second_number: int | float) -> int | float:
    answer = 0
    try:
        answer = first_number / second_number
    except ZeroDivisionError:
        print("Sorry you can't divide my zero")
        answer = 0

    return round(answer, 2)
