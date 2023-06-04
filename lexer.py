from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Program 
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('MAIN', r'main')
        
        self.lexer.add('O_BRACES', r'\{')
        self.lexer.add('C_BRACES', r'\}')
        
        # Parenthesis
        self.lexer.add('O_PAREN', r'\(')
        self.lexer.add('C_PAREN', r'\)')
        
        self.lexer.add('BEGIN', r'begin')
        
        self.lexer.add('END', r'end')
        
        # Write
        self.lexer.add('WRITE', r'write')

        # Declare Operator
        self.lexer.add('ASSIGN', r':=')
        
        # Colon
        self.lexer.add('COLON', r':')
        
        # Semi Colon
        self.lexer.add('SEMI_COLON', r';')

        # Coma
        self.lexer.add('COMA', r'\,')
        
        self.lexer.add('PLUSPLUS', r'\+\+')
        self.lexer.add('MINUSMINUS', r'--')
        

        # Arithmetic Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'/')

        # Relational Operators
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')
        self.lexer.add('LESS_THAN', r'<')
        self.lexer.add('GREATER_THAN', r'>')
        self.lexer.add('NOT_EQUAL_TO', r'!=')

        # =
        self.lexer.add('EQUAL', r'\=') # quitar backslash si truena

        # and - or
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')

        # if
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('THEN', r'then')

        # While 
        self.lexer.add('WHILE', r'while')
        self.lexer.add('DO', r'do')

        # For
        self.lexer.add('FOR', r'for')

        # Data Types - declaration
        self.lexer.add('DATA_INT', r'int')
        self.lexer.add('DATA_STRING', r'string')
        self.lexer.add('DATA_REAL', r'real')
        self.lexer.add('DATA_BOOLEAN', r'bool')
        
        # Double signs
        

        # Data Types - values
        self.lexer.add('REAL',  r"\d+(\.\d+)")
        self.lexer.add('INT', r'\d+')
        self.lexer.add('BOOLEAN', r"(true|false)")
        self.lexer.add('STRING', r'\".*\"')

        # IDs - Vars
        self.lexer.add('VAR', r'var')
        self.lexer.add('VAR_NAME', r'[a-zA-Z_][a-zA-Z_0-9]*')
        
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()