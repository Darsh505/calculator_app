import ast 
import operator

class Calculator:
    def __init__(self):
        self.operators = {
            ast.Add: operator.add, 
            ast.Sub: operator.sub, 
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

    def evaluate(self, expression):
        try:
            tree = ast.parse(expression, mode="eval")
            return self._eval_node(tree.body)
        except ZeroDivisionError:
            return "error"
        except Exception:
            return "invalid"

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            op_type = type(node.op)
            if op_type in self.operators:
                return self.operators[op_type](left, right)
            else:
                raise ValueError("Bad Operator") 

        else:
            raise ValueError("Bad Syntax")

if __name__== "__main__":
    calc = Calculator()
    print(calc.evaluate("2 + 3"))
    print(calc.evaluate("10 / 2"))
