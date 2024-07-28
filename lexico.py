alphabet_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"] # Inclui _ nos 2 alfabetos maiusculos e minusculos

alphabet_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

op_arit = ["*", "+", "-", "/"]

class Automato:
    def __init__(self):
        self.tokens = []
        self.code = []
        
    def read_file(self, file_name):
        with open(file_name, "r") as reading:
            self.code = reading.readlines()
        print(self.code)

    def analyzes_code(self):
        for string in self.code:
            self.automato_rules(string)

    def automato_rules(self, string):
        state = 1

        for letter in string:

            if state == 1: # Para o estado 1 do automato, fazer a regra de todas as transicoes
                if letter in alphabet_low or letter in alphabet_high:
                    state = 7

                elif letter in numbers:
                    state = 2

                elif letter == '"':
                    state = 9

                elif letter == '(':
                    state = 1
                    self.tokens.append(letter, "par_esq")

                elif letter == ')':
                    state = 1
                    self.tokens.append(letter, "par_dir")

                elif letter == '{':
                    state = 1
                    self.tokens.append(letter, "col_esq")

                elif letter == '}':
                    state = 1
                    self.tokens.append(letter, "col_dir")

                elif letter == "@":
                    state = 13

                elif letter == ';':
                    state = 15

                elif letter in op_arit:
                    state = 1
                    self.tokens.append(letter, "op_aritmetico")

                elif letter in ["!", "<", ">"]:# Tem que ver como fica
                    state = 1
                    self.tokens.append(string, "op_relacional")

                elif letter == ":":
                    state = 19

                elif letter == ",":
                    state = 1
                    self.tokens.append(letter, "virgula")

                else:
                    print("Erro no estado ", state)

            elif state == 19:
                if letter == "=":
                    state = 1
                    self.tokens.append(":=", "atribuicao")
        
                else:
                    print("Erro no estado ", state)

my_lex = Automato()  

my_lex.read_file("cod_teste.txt")