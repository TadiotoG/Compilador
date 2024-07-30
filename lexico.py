alphabet_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"] # Inclui _ nos 2 alfabetos maiusculos e minusculos

alphabet_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

op_arit = ["*", "+", "-", "/"]

class Automato:
    def __init__(self):
        self.tokens = []
        self.code_enter = []
        self.txt = []
        
    def read_file(self, file_name):
        with open(file_name, "r") as reading:
            self.code_enter = reading.readlines()
            #i=0
            print(self.code_enter)
            #for self.code_enter in self.code_enter:
            #    self.code.insert(i,self.code_enter.split())
            #    i += 1
            

    def analyzes_code(self):
        for string in self.code_enter:
            print(string)
            self.automato_rules(string)

    def automato_rules(self, string):
        state = 1
        i = 0
        controle = 0
        while i < len(string):
            carac = string[i]
            print("Carac:" ,carac, "State:" ,state, "Indice :" ,i)
            print(carac)
            print(state)
            if state == 1: # Para o estado 1 do automato, fazer a regra de todas as transicoes
                if carac in alphabet_low or carac in alphabet_high:
                    self.txt =  carac
                    state = 7

                elif carac in numbers:
                    self.txt =  carac
                    state = 2

                elif carac == '"':
                    self.txt =  carac
                    state = 9

                elif carac == '(':
                    state = 1
                    self.tokens.extend([carac, "par_esq"])

                elif carac == ')':
                    state = 1
                    self.tokens.extend([carac, "par_dir"])

                elif carac == '{':
                    state = 1
                    self.tokens.extend([carac, "col_esq"])

                elif carac == '}':
                    state = 1
                    self.tokens.extend([carac, "col_dir"])

                elif carac == "@":
                    self.txt =  carac
                    state = 13

                elif carac == ';':
                    self.txt =  carac
                    state = 15

                elif carac in op_arit:
                    self.txt =  carac
                    state = 1
                    self.tokens.extend([carac, "op_aritmetico"])

                elif carac in ["<", ">"]:
                    self.txt =  carac
                    state = 18    

                elif carac in ["!"]:
                    self.txt =  carac
                    state = 19

                elif carac == "=":
                    state = 1
                    self.tokens.extend([carac, "op_relacional"])

                elif carac == ":":
                    self.txt =  carac
                    state = 23

                elif carac == ",":
                    state = 1
                    self.tokens.extend([carac, "virgula"])
                else:
                    if carac != " " :
                        print("Erro no estado ", state)


            elif state == 2:
                if carac in numbers:
                    self.txt +=  carac
                    state = 2
                elif carac in ".":
                    self.txt +=  carac
                    state = 4
                else :
                    controle = 1
                    state = 1
                    self.tokens.extend([self.txt, "int"])
                    self.txt = ""

            elif state == 4:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5

            elif state == 5:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5
                else:
                    controle = 1
                    state = 1
                    self.tokens.extend([self.txt, "float"])
                    self.txt = ""
                            
            elif state == 7:
                if carac in numbers:
                    self.txt +=  carac
                    state = 7
                elif carac in alphabet_low or carac in alphabet_high:
                    self.txt  +=  carac
                    state = 7
                else:
                    controle = 1
                    state = 1 
                    self.tokens.extend([self.txt, "id"])
                    self.txt = ""

            elif state == 9:
                if carac in '"':
                    self.txt +=  carac
                    state = 1
                    self.tokens.extend([self.txt, "string"])
                    self.txt = ""
                else:
                    self.txt +=  carac
                    state = 9

            elif state == 13:
                if carac in '\n':
                    state = 1
                    self.txt +=  carac
                    self.tokens.extend([self.txt, "comentario"])
                    self.txt = ""
                else:
                    self.txt +=  carac
                    state = 13

            elif state == 15:
                if carac in "\n":
                    state = 1
                    self.txt +=  carac
                    self.tokens.extend([self.txt, "fim_linha"])
                    self.txt = ""

            elif state == 18:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.extend([self.txt, "op_relacional"])
                    self.txt = ""
                else:
                    controle = 1
                    state = 1
                    self.tokens.extend([self.txt, "op_relacional"])
                    self.txt = ""

            elif state == 19:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.extend([self.txt, "op_relacional"])
                    self.txt = ""

            elif state == 23:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.extend([self.txt, "atribuicao"])
                    self.txt = ""

            else:
                print("Erro no estado ", state)
            
            if controle == 0:
                i += 1  # Incrementar o índice para a próxima iteração
            else:
                controle = 0
my_lex = Automato()  

my_lex.read_file("cod_teste.txt")
my_lex.analyzes_code()
print(my_lex.tokens)