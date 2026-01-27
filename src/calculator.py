class calculator:
    def evaluate(self, expression):
        try:
            result = eval(expression)
            return result

        except ZeroDivisionError:
            return "error: division by zero not possible"
        except Exception:
            return "invalid expression"

def main():
    calc = calculator()

    while True:
        expression = input("Enter an expression:")

        if expression.lower() == "exit":
            print("goodbye!")
            break

        result = calc.evaluate(expression)
        print("result:", result)

if __name__ == "__main__":
    main()            
