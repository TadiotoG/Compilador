import lexico

my_lex = lexico.Automato()  

my_lex.read_file("cod_teste3.txt")
my_lex.analyzes_code()
print(my_lex.tokens)