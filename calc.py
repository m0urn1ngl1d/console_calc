def check_input():
    in_box = input("Input the equation: ")
    if " " not in in_box and "q" not in in_box:
        print("WRITE WITH SPACES")
        return check_input()
    return in_box.split()

def el_of_equation(res):
    math_operators = ("+", "-", "*", "/", "^")
    key_input = check_input()
    if key_input == ["q"]:
        return "q"
    key_input.extend(res)
    index = None
    op = None
    for i in range(len(key_input)):
        if key_input[i] in math_operators:
            index = i
            op = key_input[i]
            break   
    left = float(key_input[index - 1])
    right = float(key_input[index + 1])
    # print(key_input)
    return op, left, right
    

def calculate(res=[]):
    oper_tup = el_of_equation(res)
    if len(res) >= 1:
        res.remove(res[0])
    if "q" in oper_tup:
        print()
        return "BYE!"
    op, left, right = oper_tup
    if op == "+":
        res.append(left + right)
    if op == "-":
        res.append(left - right)
    if op == "*":
        res.append(left * right)
    if op == "^":
        res.append(left ** right)
    if op == "/":
        try:
            res.append(left / right)
        except ZeroDivisionError:
            print("DIVISION BY 0 IS UNEXCEPTABLE")
            return calculate(res)
    print("Result =", *res)
    return calculate()


result = calculate()
print(result)
