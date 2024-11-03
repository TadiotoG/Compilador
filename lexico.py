from sintatico import Sintatico


alphabet_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"] # Inclui _ nos 2 alfabetos maiusculos e minusculos

alphabet_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]

full_alphabet = alphabet_low + alphabet_high

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
            # #print(self.code_enter)
            # for self.code_enter in self.code_enter:
            #    self.code.insert(i,self.code_enter.split())
            #    i += 1
            

    def analyzes_code(self):
        self.code_enter[-1] += '\n'
        for linha in range(len(self.code_enter)):
            self.automato_rules(self.code_enter[linha], linha)

    def automato_rules(self, string, linha):
        state = 1
        i = 0
        controle = 0
        while i < len(string):
            carac = string[i]

            # #print("Estado:", state)

            if state == 1: # Para o estado 1 do automato, fazer a regra de todas as transicoes
                if carac == "o":
                    self.txt = carac
                    state = 61

                elif carac == "w":
                    self.txt = carac
                    state = 80

                elif carac == "n":
                    self.txt = carac
                    state = 85

                elif carac == "e":
                    self.txt = carac
                    state = 73

                elif carac == "a":
                    self.txt = carac
                    state = 70

                elif carac == "+":
                    self.txt = carac
                    state = 50

                elif carac == "-":
                    self.txt = carac
                    state = 52

                elif carac == "i":
                    self.txt = carac
                    state = 26

                elif carac == "f":
                    self.txt = carac
                    state = 27

                elif carac == "s":
                    self.txt = carac
                    state = 28

                elif carac == "b":
                    self.txt = carac
                    state = 29

                elif carac in full_alphabet:
                    self.txt = carac
                    state = 7

                elif carac in numbers:
                    self.txt = carac
                    state = 2

                elif carac == '"':
                    self.txt = carac
                    state = 9

                elif carac == '(':
                    state = 1
                    self.tokens.append([carac, "par_esq"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == ')':
                    state = 1
                    self.tokens.append([carac, "par_dir"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == '{':
                    state = 1
                    self.tokens.append([carac, "col_esq"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == '}':
                    state = 1
                    self.tokens.append([carac, "col_dir"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == "@":
                    self.txt =  carac
                    state = 13

                elif carac == ';':
                    self.txt =  carac
                    self.tokens.append([self.txt, "fim_linha"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    state = 1
                    self.txt = ""

                elif carac == '\n':
                    self.txt =  carac
                    self.tokens.append([self.txt, "ContraBarraN"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    state = 1
                    self.txt = ""

                elif carac in ("*", "/"):
                    self.txt =  carac
                    state = 1
                    self.tokens.append([carac, "op_aritmetico"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac in ["<", ">"]:
                    self.txt =  carac
                    state = 18    

                elif carac in ["!"]:
                    self.txt =  carac
                    state = 19

                elif carac == "=":
                    state = 1
                    self.tokens.append([carac, "op_relacional"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                elif carac == ":":
                    self.txt =  carac
                    state = 23

                elif carac == ",":
                    state = 1
                    self.tokens.append([carac, "virgula"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")

                else:
                    if carac != " " and carac != "\n":
                        self.txt +=  carac
                        #print("Erro na linha ", linha+1, "  palavra:", self.txt, "  estado:", state,  "\n")
                        state = 1


            elif state == 2:
                if carac in numbers:
                    self.txt +=  carac
                    state = 2
                elif carac in ".":
                    self.txt +=  carac
                    state = 4
                    
                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "int"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 4:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5

                else:
                    while i < len(string) and (string[i] != ' ' and string[i] != '\n'):
                        self.txt += string[i]
                        i+=1
                    #print("Erro na linha ", linha+1, "  palavra:", self.txt, "  estado:", state,  "\n")
                    state = 1
                    controle = 1

            elif state == 5:
                if carac in numbers:
                    self.txt +=  carac
                    state = 5

                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "float"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                            
            elif state == 7:
                if carac in numbers:
                    self.txt +=  carac
                    state = 7
                elif carac in full_alphabet:
                    self.txt  +=  carac
                    state = 7
                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 9:
                if carac in '"':
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "string"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    self.txt +=  carac
                    state = 9

            elif state == 13:
                if carac == "\n":
                    state = 1
                    self.txt +=  carac
                    self.tokens.append([self.txt, "comentario"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                    controle = 1

                else:
                    self.txt +=  carac
                    state = 13

            elif state == 18:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    controle = 1
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 19:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "op_relacional"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    while i < len(string) and (string[i] != ' ' and string[i] != '\n'):
                        self.txt += string[i]
                        i+=1
                    #print("Erro na linha ", linha+1, "  palavra:", self.txt, "  estado:", state,  "\n")
                    state = 1
                    controle = 1

            elif state == 23:
                if carac == "=":
                    self.txt +=  carac
                    state = 1
                    self.tokens.append([self.txt, "atribuicao"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    while i < len(string) and (string[i] != ' ' and string[i] != '\n'):
                        self.txt += string[i]
                        i+=1
                    #print("Erro na linha ", linha+1, "  palavra:", self.txt, "  estado:", state,  "\n")
                    state = 1
                    controle = 1

            elif state == 26:
                if carac == "n":
                    state = 30
                    self.txt += carac

                elif carac == "f":
                    state = 55
                    self.txt += carac

                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 27:
                if carac == "l":
                    state = 33
                    self.txt += carac

                elif carac == "o":
                    state = 77
                    self.txt += carac

                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 28:
                if carac == "t":
                    state = 38
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 29:
                if carac == "o":
                    state = 44
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 30:
                if carac == "t":
                    state = 31
                    self.txt += carac

                elif carac == "p":
                    state = 57
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 31:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "idInt"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 7
                    self.txt += carac

            elif state == 33:
                if carac == "o":
                    state = 34
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 34:
                if carac == "a":
                    state = 35
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 35:
                if carac == "t":
                    state = 36
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 36:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "idFloat"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 7
                    self.txt += carac

            elif state == 38:
                if carac == "r":
                    state = 39
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 39:
                if carac == "i":
                    state = 40
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 40:
                if carac == "n":
                    state = 41
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 41:
                if carac == "g":
                    state = 42
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 42:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "idString"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 7
                    self.txt += carac

            elif state == 44:
                if carac == "o":
                    state = 45
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 45:
                if carac == "l":
                    state = 46
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 46:
                if carac == "e":
                    state = 47
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 47:
                if carac == "a":
                    state = 48
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 48:
                if carac == "n":
                    state = 49
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 49:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "idBoolean"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 7
                    self.txt += carac

            elif state == 50:
                if carac == "+":
                    self.txt += "+"
                    state = 1 
                    self.tokens.append([self.txt, "incremento"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 1
                    self.tokens.append([self.txt, "op_aritmetico"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    controle = 1
                    self.txt = ""

            elif state == 52:
                if carac == "-":
                    self.txt += "-"
                    state = 1 
                    self.tokens.append([self.txt, "decremento"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

                else:
                    state = 1
                    self.tokens.append([self.txt, "op_aritmetico"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    controle = 1
                    self.txt = ""

            elif state == 55:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "if"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 57:
                if carac == "u":
                    state = 58
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 58:
                if carac == "t":
                    state = 59
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 59:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "input"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 61:
                if carac == "r":
                    state = 62
                    self.txt += carac

                elif carac == "u":
                    state = 64
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 62:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "or"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 64:
                if carac == "t":
                    state = 65
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 65:
                if carac == "p":
                    state = 66
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 66:
                if carac == "u":
                    state = 67
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 67:
                if carac == "t":
                    state = 68
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

            elif state == 68:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "output"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 70:
                if carac == "n":
                    state = 71
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 71:
                if carac == "d":
                    state = 72
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 72:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "and"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 73:
                if carac == "l":
                    state = 74
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 74:
                if carac == "s":
                    state = 75
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 75:
                if carac == "e":
                    state = 76
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 76:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "else"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 77:
                if carac == "r":
                    state = 78
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 78:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "for"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 85:
                if carac == "o":
                    state = 86
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 86:
                if carac == "t":
                    state = 87
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 87:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "not"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            elif state == 80:
                if carac == "h":
                    state = 81
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 81:
                if carac == "i":
                    state = 82
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 82:
                if carac == "l":
                    state = 83
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 83:
                if carac == "e":
                    state = 84
                    self.txt += carac
                    
                elif carac in full_alphabet:
                    state = 7
                    self.txt += carac

                else:
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "id"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""

            elif state == 84:
                if not (carac in full_alphabet or carac in numbers):
                    controle = 1
                    state = 1 
                    self.tokens.append([self.txt, "while"])
                    #print("Código encontrado: ", self.tokens[-1][0], "    Token: ", self.tokens[-1][1], "\n")
                    self.txt = ""
                else:
                    state = 7
                    self.txt += carac

            if controle == 0:
                i += 1  # Incrementar o índice para a próxima iteração

            else:
                controle = 0
my_lex = Automato()  

my_lex.read_file("cod_teste3.txt")
my_lex.analyzes_code()

##print(my_lex.tokens)
tokens_solo = []
for i in my_lex.tokens:
    if (i[1] != 'ContraBarraN' and i[1] != "comentario"):
        tokens_solo.append(i[1])
##print(tokens_solo)
Sintatico(tokens_solo)