alphabet_low = ["_","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"] # Inclui _ nos 2 alfabetos maiusculos e minusculos

alphabet_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

op_arit = ["*", "+", "-", "/"]

class Automato:
    def __init__(self):
        self.tokens = []
        self.code_enter = []
        self.code = []
        
    def read_file(self, file_name):
        with open(file_name, "r") as reading:
            self.code_enter = reading.readlines()
            i=0
            for self.code_enter in self.code_enter:
                self.code.insert(i,self.code_enter.split())
                i += 1
            print(self.code)

    def analyzes_code(self):
        for string in self.code:
            self.automato_rules(string)

    def automato_rules(self, string):
        state = 1

        for letter in string:
            #letter_space = ' '.join([char for char in letter]) Fui burro nao precisa disso
            print(letter)
            for carac in letter:
                print(carac)
                print(state)
                if state == 1: # Para o estado 1 do automato, fazer a regra de todas as transicoes
                    if carac in alphabet_low or carac in alphabet_high:
                        state = 7

                    elif carac in numbers:
                        state = 2

                    elif carac == '"':
                        state = 9

                    elif carac == '(':
                        state = 1
                        self.tokens.extend([carac, "par_esq"])

                    elif carac == ')':
                        state = 1
                        self.tokens.extend([carac, "par_dir"])

                    elif carac == '{':
                        print("entrou")
                        state = 1
                        self.tokens.extend([carac, "col_esq"])

                    elif carac == '}':
                        state = 1
                        self.tokens.extend([carac, "col_dir"])

                    elif carac == "@":
                        state = 13

                    elif carac == ';':
                        state = 15

                    elif carac in op_arit:
                        state = 1
                        self.tokens.extend([letter, "op_aritmetico"])

                    elif carac in ["<", ">"]:
                        state = 18    

                    elif carac in ["!"]:
                        state = 19

                    elif carac == "=":
                        state = 1
                        self.tokens.extend([letter, "op_relacional"])

                    elif carac == ":":
                        state = 23

                    elif carac == ",":
                        state = 1
                        self.tokens.extend([letter, "virgula"])
                    else:
                        print("Erro no estado ", state)

    
                elif state == 2:
                    if carac in numbers:
                        state = 2
                    elif carac in ".":
                        state = 4
                    else :
                        state = 1
                        self.tokens.extend([letter, "int"])

                elif state == 4:
                    if carac in numbers:
                        state = 5

                elif state == 5:
                    if carac in numbers:
                        state = 5
                    else:
                        state = 1
                        self.tokens.extend([letter, "float"])
                               
                elif state == 7:
                    if carac in numbers:
                        state = 7
                    elif carac in alphabet_low or carac in alphabet_high:
                        state = 7
                    else:
                        state = 1 
                        self.tokens.extend([letter, "id"])

                elif state == 9:
                    if carac in '"':
                        state = 1
                        self.tokens.extend([letter, "string"])
                    else:
                        state = 9

                elif state == 13:
                    if carac in "\n":
                        state = 1
                        self.tokens.extend([letter, "comentario"])
                    else:
                        state = 13

                elif state == 15:
                    if carac in "\n":
                        state = 1
                        self.tokens.extend([letter, "fim_linha"])
                    else:
                        print("Erro 15")

                elif state == 18:
                    if carac == "=":
                        state = 1
                        self.tokens.extend([letter, "op_relacional"])
                    else:
                        state = 1
                        self.tokens.extend([letter, "op_relacional"])

                elif state == 19:
                    if carac == "=":
                        state = 1
                        self.tokens.extend([letter, "atribuicao"])

                elif state == 23:
                    if carac == "=":
                        state = 1
                        self.tokens.extend([letter, "atribuicao"])

                else:
                    print("Erro no estado ", state)

my_lex = Automato()  

my_lex.read_file("cod_teste.txt")
my_lex.analyzes_code()
print(my_lex.tokens)