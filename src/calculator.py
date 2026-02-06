import ast 
import operator

class Calculator:
    def __inite__(self):
        self.operators = {
            ast.Add: operator.add, 
            ast.Sub: operator.sub, 
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

    def evaluate(self, expression):
        try:
            tree = ast.parse(expresion, mode="eval")
            return self._eval_node(tree.body)
        except ZeroDivisionError:
            return "error"
        except Exception:
            return "invalid"

    def _eval_node(self, node):
        if isinstance(node, ast.constant):
            return node.n

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

