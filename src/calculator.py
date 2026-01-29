import ast 
import operator

class calculator:
    def __inite__(self):
        self.operators = {
            ast.add: operator.add, 
            ast.sub: operator.sub, 
            ast.mult: operator.mul,
            ast.div: operator.truediv
        }

    def evaluate(self, expression):
        try:
            tree = ast.parse(expresion, mode="eval")
            return self._eval_node(tree.body)
        except ZeroDivisionError:
            return "error"
        except Exception:
            return "inavlid"

    def _eval_node(self, node):
        if isinstance(node, ast.Num):
            return node.n

        if isinstance(self, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            op_type = type(node.op)
            if op_type in self.operators:
                return self.operators[op_type](left, right)
            else:
                raise ValueError("Bad Operator") 

        else:
            raise ValueError("Bad Syntax")

