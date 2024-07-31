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
            # i=0
            # print(self.code_enter)
            # for self.code_enter in self.code_enter:
            #    self.code.insert(i,self.code_enter.split())
            #    i += 1
            

    def analyzes_code(self):
        for string in self.code_enter:
            print(string)
            string = string + " "
            self.automato_rules(string)

    def print_tokens(self):
        for token in self.tokens:
            print("Código encontrado: ", token[0], "    Token: ", token[1], "\n")

    def automato_rules(self, string):
        state = 1
        i = 0
        controle = 0
        while i < len(string):
            carac = string[i]
            print("Carac:" ,carac, "State:" ,state, "Indice :" ,i)
            # print(carac)
            # print(state)
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
                    self.tokens.append([carac, "par_esq"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == ')':
                    state = 1
                    self.tokens.append([carac, "par_dir"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == '{':
                    state = 1
                    self.tokens.append([carac, "col_esq"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == '}':
                    state = 1
                    self.tokens.append([carac, "col_dir"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == "@":
                    self.txt =  carac
                    state = 13

                elif carac == ';':
                    self.txt =  carac
                    state = 15

                elif carac in op_arit:
                    self.txt =  carac
                    state = 1
                    self.tokens.append([carac, "op_aritmetico"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac in ["<", ">"]:
                    self.txt =  carac
                    state = 18    

                elif carac in ["!"]:
                    self.txt =  carac
                    state = 19

                elif carac == "=":
                    state = 1
                    self.tokens.append([carac, "op_relacional"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == ":":
                    self.txt =  carac
                    state = 23

                elif carac == ",":
                    state = 1
                    self.tokens.append([carac, "virgula"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                else:
                    if carac != " " and carac != "\n":
                        self.txt +=  carac
                        print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                        state = 1


            elif state == 2:
                print("entrou")
                if carac in numbers:
                    self.txt +=  carac
                    state = 2
                elif carac in ".":
                    self.txt +=  carac
                    state = 4

                elif carac in alphabet_low or carac in alphabet_high:
                    self.txt +=  carac
                    print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                    state = 1
                    
                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "int"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 4:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5

            elif state == 5:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5

                elif carac in alphabet_low or carac in alphabet_high:
                    self.txt +=  carac
                    print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                    state = 1
                    controle = 1

                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "float"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
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
                    self.tokens.append([self.txt, "id"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 9:
                if carac in '"':
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "string"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    self.txt +=  carac
                    state = 9

            elif state == 13:
                if carac in '\n':
                    state = 1
                    self.txt +=  carac
                    self.tokens.append([self.txt, "comentario"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    self.txt +=  carac
                    state = 13

            elif state == 15:
                if carac in "\n":
                    state = 1
                    self.txt +=  carac
                    self.tokens.append([self.txt, "fim_linha"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    self.txt +=  carac
                    print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                    state = 1

            elif state == 18:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 19:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    self.txt +=  carac
                    print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                    state = 1
                    controle = 1

            elif state == 23:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "atribuicao"])
                    print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    self.txt +=  carac
                    print("Erro no estado ", state, "  caracter:", self.txt, "\n")
                    state = 1
                    controle = 1
                
            if controle == 0:
                i += 1  # Incrementar o índice para a próxima iteração
            else:
                controle = 0
my_lex = Automato()  

my_lex.read_file("cod_teste2.txt")
my_lex.analyzes_code()

# my_lex.print_tokens()
print(my_lex.tokens)