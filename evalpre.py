""" Evaluate integer expressions with equal operator        precedence. Supported operators: +,-,*,/.

Example: evalpre('1+2*3') returns 9.

Author: Hans Martin Aannestad

"""

# Integer class with equal operator precedence
class Int:
    def __init__(self,val):
        self.val = val

    # / as addition
    def __floordiv__(self,b):
        return Int(self.val + b.val)

    # % as subtraction
    def __mod__(self,b):
        return Int(self.val - b.val)
    
    # * as multiplication
    def __mul__(self,b):
        return Int(self.val * b.val)

    # // as Division
    def __truediv__(self,b):
        return Int(self.val / b.val)

# Function for expression evaluation
def evalpre(expression):
    """Evaluate integer expression (+-*/)"""

    # Replace operators
    expression = expression.replace("+","//").replace       ("-","%")

    # Wrap expression to Int class
    expr = ""
    is_Int = False
    for i in expression:
        if i in "0123456789" and not is_Int:
            expr += "Int("
            is_Int = True
        if is_Int and i not in "0123456789":
            expr += ")"
            is_Int = False
        expr += i
    if is_Int:
        expr += ")"

    # Evaluate Int expression
    return eval(expr).val