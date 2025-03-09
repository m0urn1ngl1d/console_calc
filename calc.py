def check_input():
    in_box = input("Input the equation: ")
    if " " not in in_box and "q" not in in_box:
        print("WRITE WITH SPACES")
        return check_input()
    return in_box.split()

def el_of_equation(res):
    math_operators = ("+", "-", "*", "/", "^")
    key_input = check_input()
    if "q" in key_input:
        return "q"
    key_input.extend(res)
    index = None
    op = None
    for i, el in enumerate(key_input):
        if el in math_operators:
            index = i
            op = el
            break
    try:
        left = float(key_input[index - 1])
        right = float(key_input[index + 1])
    except ValueError:
        print("OOPS! NOT A NUMBER")
        return None
    # print(key_input)
    return op, left, right

def calculate(res=[]):
    oper_tup = el_of_equation(res)
    if oper_tup == "q":
        print()
        return "BYE!"
    if oper_tup is None:
        return calculate()
    res.clear()
    op, left, right = oper_tup
    if op == "+":
        res.append(left + right)
    elif op == "-":
        res.append(left - right)
    elif op == "*":
        res.append(left * right)
    elif op == "^":
        res.append(left ** right)
    elif op == "/":
        try:
            res.append(left / right)
        except ZeroDivisionError:
            print("DIVISION BY 0 IS UNEXCEPTABLE")
            return calculate(res)
    print("Result =", *res)
    return calculate()


print(calculate())
