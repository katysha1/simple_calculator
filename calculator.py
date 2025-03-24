def calculator():

    while True:
        try:
            num1 = float(input("число 1: "))
            op = input("действие (+, -, *, /, **): ")
            if op == "**":
                result=num1**num1

            else:
                num2 = float(input("число 2: "))

                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    result = num1 / num2
                else:
                    print("Неверный оператор. Пожалуйста, попробуйте еще раз.")
                    continue

            print(f"Результат: {result}")
            break

        except ValueError:
            print("Ошибка. Пожалуйста, введите числа.")
        except ZeroDivisionError:
            print("На ноль делить нельзя.")

if __name__ == "__main__":
    calculator()