# value, type
variables = {}

class Statements:
    def __init__(self, nodes):
        self.nodes = nodes

    def eval(self):
        for node in self.nodes:
            print(node)
            node.eval()
            
class Block:
    def __init__(self, nodes):
        self.nodes = nodes
        
    def eval(self):
        for node in self.nodes:
            print(node)
            node.eval()
            
class Real():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)
    
class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)
    
class StringConcat:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    
    def eval(self):
        return str(self.str1.value) + str(self.str2.value)

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()
    
class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
    
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()
    
class LessEqual(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()

class GreaterEqual(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()
    
class LessThan(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()
    
class GreaterThan(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()
    
class NotEqualTo(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()
    
class IsEqual(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()
    
class And(BinaryOp):
    def eval(self):
        return self.left.eval() and self.right.eval()
    
class Or(BinaryOp):
    def eval(self):
        return self.left.eval() or self.right.eval()
    
class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        if (isinstance(self.value, str)):
            print(self.value.getstr()[1:-1])
        else: 
            print(self.value.eval())

class Assign():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        variables[self.name] = self.value.eval()

class Declare:
    def __init__(self, name):
        self.name = name

    def eval(self):
        variables[self.name] = None

class Variable():
    def __init__(self, name):
        self.name = name
    
    def eval(self):
        if self.name in variables.keys():
            return variables[self.name]
        else: 
            raise RuntimeError("Variable not declared:", self.name)
        
class Variable2():
    def __init__(self, name):
        self.name = name
    
    def eval(self):
        if self.name in variables.keys():
            return variables[self.name][0]
        else: 
            raise RuntimeError('Variable: ', self.name,' not declared.')
        
class If():
    def  __init__(self, condition, body, else_block = None):
       self.condition = condition
       self.body = body
       self.else_block = else_block
    
    def eval(self):
       if self.condition.eval() == True:
           return self.body.eval()
       elif self.else_block is not None:
           return self.else_block.eval()
       # return None

class ForCycle:
    def __init__(self, identifier, condition, increment, body):
        self.id = identifier
        self.condition = condition
        self.increment = increment
        self.body = body
    
    def eval(self):
        while(self.condition.eval()):
            self.body.eval()
            self.increment.eval()

class WhileCycle:
    def __init__(self, condition, func):
        self.condition = condition
        self.func = func

    def eval(self):
        while(self.condition.eval()):
            self.func.eval()

class Program():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("Successful program")