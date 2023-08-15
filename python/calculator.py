import re

arr = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(arg):
    if len(arg) > 5:
        print("Error: Too many problems.")
        return

    for expression in arg:
        if re.search(r"[^\+\-\d\s]", expression):
            print("Error: Operator must be '+' or '-'.")
            return
        if re.search(r"\d{5,}", expression):
            print("Error: Numbers cannot be more than four digits.")
            return
        if re.search(r"\d+\s\d+", expression):
            print("Error: Numbers must only contain digits.")
            return

        numbers = re.findall(r"\d+", expression)
        operator = re.findall(r"[\+\-]", expression)[0]
        num1 = int(numbers[0])
        num2 = int(numbers[1])

        if operator == "+":
            result = num1 + num2
        else:
            result = num1 - num2

        max_width = max(len(numbers[0]), len(numbers[1])) + 2
        arranged = f"{num1:>{max_width}}\n{operator} {num2:>{max_width-2}}\n{'-' * max_width}\n{result:>{max_width}}"
        print(arranged)


arithmetic_arranger(arr)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
