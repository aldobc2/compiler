# Aldo Berain Cardenas || A00827874

from lexer import Lexer
from parserFile import Parser

fname = "input2.txt"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()