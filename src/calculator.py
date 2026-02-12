# This file contains the core calculation logic.
# It safely evaluates mathematical expressions using AST
# instead of Python's eval() for security.

import ast 
import operator

# Calculator class handles parsing and evaluating expressions

class Calculator:
    def __init__(self):

        # Map allowed AST operator nodes to actual math functions
        # This limits what operations are allowed in expressions

        self.operators = {
            ast.Add: operator.add, 
            ast.Sub: operator.sub, 
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }

    def evaluate(self, expression):

        # Entry point for evaluation
        # Takes a string expression and returns the calculated result

        try:

            # Convert expression string into an AST (abstract syntax tree)

            tree = ast.parse(expression, mode="eval")
            return self._eval_node(tree.body)
        except ZeroDivisionError:
            return "error"
        except Exception:
            return "invalid"

    def _eval_node(self, node):

        # Recursively evaluates a single AST node
        # This function walks through the expression tree

        # If the node is a number (constant), return its value

        if isinstance(node, ast.Constant):
            return node.value

        # If the node is a binary operation (e.g. +, -, *, /)

        if isinstance(node, ast.BinOp):

            # Evaluate left and right sides first, then apply the operator

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
