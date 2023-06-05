from rply import ParserGenerator
from AbsSynTree import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Tokens
            ['PROGRAM', 'MAIN', 'BEGIN', 'END', 'WRITE',
             'O_PAREN', 'C_PAREN', 'O_BRACES', 'C_BRACES', 'ASSIGN',
             'SEMI_COLON', 'COMA', 'SUM', 'SUB', 'MULT', 'DIV',
             'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN', 'NOT_EQUAL_TO', 
             'IS_EQUAL', 'EQUAL', 'AND', 'OR', 'IF', 'ELSE', 'THEN', 'WHILE', 'DO', 'FOR', 
             'DATA_REAL', 'DATA_INT', 'DATA_STRING', 'DATA_BOOLEAN', 'REAL', 'INT',
             'STRING', 'BOOLEAN', 'VAR_NAME', 'VAR', 'COLON', 'PLUSPLUS', 'MINUSMINUS'],
            
            # Precedencia ascendente para reglas de produccion
            precedence = [
            ('left', ['LESS_THAN', 'GREATER_THAN']),
            ('left', ['LESS_EQUAL', 'GREATER_EQUAL']),
            ('left', ['IS_EQUAL', 'NOT_EQUAL_TO']),
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV']),
            ]
        )

    def parse(self):
        # main program
        #@self.pg.production("program : PROGRAM MAIN O_BRACES defs BEGIN SEMI_COLON statements END SEMI_COLON C_BRACES")
        @self.pg.production("program : PROGRAM MAIN O_BRACES block C_BRACES")              
        def program(p):
            return p[3]
        
        @self.pg.production("block : start start")
        @self.pg.production("block : start")
        def block_all(p):
            return Statements(p)
        
        @self.pg.production("start : defs")
        def process_defs(p):
            return p[0]
        
        @self.pg.production("start : BEGIN SEMI_COLON statements END SEMI_COLON")
        def one_block(p):
            return p[2]      

        @self.pg.production("statements : statements statements") # second statements is a list
        @self.pg.production("statements : proc")
        @self.pg.production("statements : exp")
        def statements_all(p):
            #print(p)
            return Statements(p)
        
        # Declara
        @self.pg.production('VAR_LIST : VAR_NAME')
        def varDeclaration(p):
            return [p[0].getstr()]
        
        @self.pg.production('VAR_LIST : VAR_NAME COMA VAR_LIST')
        def varDeclarationList(p):
            return [p[0].getstr()] + p[2]

        @self.pg.production('defs : VAR VAR_LIST COLON dataType SEMI_COLON')
        def varDec(p):
            VAR_LIST = p[1]
            # print(p[1])
            # print(p[2])
            # print(p[3])
            # print(p[4])
            for n in VAR_LIST:
                return Declare(n)
        
        # asigna
        @self.pg.production('proc : VAR_NAME ASSIGN exp SEMI_COLON')
        def varAssign(p):
            return Assign(p[0].getstr(), p[2])
        
        @self.pg.production('exp : VAR_NAME')
        def id(p):
            return Variable(p[0].getstr())
        
        # Paren
        @self.pg.production('exp : O_PAREN exp C_PAREN')
        def exp_parenths(p):
            return p[1]

        # Oper Arit
        @self.pg.production('exp : exp SUM exp')
        @self.pg.production('exp : exp SUB exp')
        @self.pg.production('exp : exp MULT exp')
        @self.pg.production('exp : exp DIV exp')
        def exp_arithmetics(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
        
        @self.pg.production('exp : VAR_NAME MINUSMINUS SEMI_COLON')
        @self.pg.production('exp : VAR_NAME PLUSPLUS SEMI_COLON')
        def exp_ari(p):
            left = p[0]
            operator = p[1]
            if operator.gettokentype() == 'MINUSMINUS':
                return SubSub(p[0])
            else:
                return PluPlu(p[0])
            
        # Opera Rels
        # condicionales de comparacion
        @self.pg.production('exp : exp LESS_EQUAL exp')
        @self.pg.production('exp : exp GREATER_EQUAL exp')
        @self.pg.production('exp : exp LESS_THAN exp')
        @self.pg.production('exp : exp GREATER_THAN exp')
        @self.pg.production('exp : exp NOT_EQUAL_TO exp')
        @self.pg.production('exp : exp IS_EQUAL exp')
        def exp_relationals(p):
            left = p[0]
            right = p[2]
            relOperator = p[1]
            if relOperator.gettokentype() == 'LESS_EQUAL':
                return LessEqual(left, right)
            elif relOperator.gettokentype() == 'GREATER_EQUAL':
                return GreaterEqual(left, right)
            elif relOperator.gettokentype() == 'LESS_THAN':
                return LessThan(left, right)
            elif relOperator.gettokentype() == 'GREATER_THAN':
                return GreaterThan(left, right)
            elif relOperator.gettokentype() == 'NOT_EQUAL_TO':
                return NotEqualTo(left, right)
            elif relOperator.gettokentype() == 'IS_EQUAL':
                return IsEqual(left, right)
        
        # datatype
        @self.pg.production('dataType : DATA_INT')
        @self.pg.production('dataType : DATA_STRING ')
        @self.pg.production('dataType : DATA_REAL')
        @self.pg.production('dataType : DATA_BOOLEAN')
        def dataTypes(p):
            return p[0]
        
        # Tipo num
        @self.pg.production('exp : REAL')
        @self.pg.production('exp : INT')
        def number(p):
            if (p[0].gettokentype() == 'REAL'):
                return Real(p[0].value)
            return Number(p[0].value)
        
        # String exps
        @self.pg.production('exp : STRING')
        def string(p):
            return String(p[0].value[1:-1])
        
        @self.pg.production('exp : BOOLEAN')
        def boolean(p):
            return Boolean(p[0].value)
        
        # Write
        @self.pg.production('proc : WRITE exp SEMI_COLON')
        def proc(p):
            return Print(p[1])
            
        # and | or 
        @self.pg.production('exp : exp AND exp')
        @self.pg.production('exp : exp OR exp')
        def exp_logic(p):
            left = p[0]
            right = p[2]
            if (p[1].gettokentype() == 'AND'):
                return And(left, right)
            else:
                return Or(left, right)
            
        #if
        @self.pg.production('proc : IF exp THEN O_BRACES statements C_BRACES')
        @self.pg.production('proc : IF exp THEN O_BRACES statements C_BRACES ELSE O_BRACES statements C_BRACES')
        def ifProcs(p):
            if len(p) > 6:
                return If(p[1], p[4], p[8])
            else:
                return If(p[1], p[4])
            
        #while
        @self.pg.production('proc : WHILE O_PAREN exp C_PAREN DO O_BRACES statements C_BRACES')
        def whileLoop(p):
            return WhileCycle(p[2], p[6])
        
        # Assign for FOR cycles
        @self.pg.production('assignFor : VAR_NAME ASSIGN exp SEMI_COLON')
        def varAssign(p):
            return Assign(p[0].getstr(), p[2])
        
        #for 
        # segundo exp de condicional cambiar nombre
        @self.pg.production('proc : FOR O_PAREN VAR_NAME ASSIGN exp SEMI_COLON exp SEMI_COLON VAR_NAME PLUSPLUS C_PAREN O_BRACES statements C_BRACES')
        @self.pg.production('proc : FOR O_PAREN VAR_NAME ASSIGN exp SEMI_COLON exp SEMI_COLON VAR_NAME MINUSMINUS C_PAREN O_BRACES statements C_BRACES')
        def forLoop(p): 
            return ForCycle(p[2], p[4], p[6], p[8], p[9], p[12])      
        

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()