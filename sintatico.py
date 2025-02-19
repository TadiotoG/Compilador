# Aluno: Gabriel Tadioto Oliveira e David Antonio Brocardo
# Trabalho de Compiladores - 2

import csv
from lexico import Automato

class Sintatico:
    def __init__(self, tokens, cod_real):
        self.entrada = tokens
        self.codigo_real = cod_real
        self.pilha = []
        self.regras = []
        self.pilha.append('$')
        self.entrada.append('$')
        self.pilha.append('<program>')
        self.read_file('Tabela_Regras.csv')
        # print("Entrada: ", self.entrada)
        self.analise_sintatica()
        self.erro = 0
        self.tabela_laco= {}
        self.tabela_simbolos = {}
        
    
    def procura_cod_tab_sim(self, string):
        for i in range(len(self.tabela_simbolos["cod"])):
            if(self.tabela_simbolos["cod"][i] == string):
                return i
        return -1
        
    def append_tab_simbolo(self, token, cod, util):
            self.tabela_simbolos["token"].append(token)
            self.tabela_simbolos["cod"].append(cod)
            self.tabela_simbolos["utilizada"].append(util)

    def append_tab_simbolo_laco(self, cod, num):
            self.tabela_laco["cod"].append(cod)
            self.tabela_laco["laco"].append(num)
            return
    
    def verifica_atribuicao(self, pos, linha, i):
            self.tabela_simbolos["utilizada"][pos] = True
            if(i == 3):
                pos_print = 1
            else:
                pos_print = 0
            
            while(self.entrada[i-1] != "fim_linha" or i > 100):
                if(self.tabela_simbolos["token"][pos] == "idInt" or self.tabela_simbolos["token"][pos] == "idFloat"): # se o cara é int ou float
                    if (self.entrada[i] == "id"):
                        pos2 = self.procura_cod_tab_sim(self.codigo_real[i])

                        if(self.tabela_simbolos["token"][pos2] == "idString"): # se o proximo a ser atribuido a ele é uma string
                            print(f"Atribuição de variavel string para variavel numérica {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                        elif(self.tabela_simbolos["token"][pos2] == "idBoolean"): # se o proximo a ser atribuido a ele é boolean
                            print(f"Atribuição de variavel boleano para variavel numérica {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                        elif(self.tabela_simbolos["token"][pos] == "idInt" and self.tabela_simbolos["token"][pos2] == "idFloat"): # se ele é um inteiro a var ser atribuido a ele é float
                            print(f"Atribuição de variavel float para variavel inteira {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        else:
                            i=i+2

                    elif(self.entrada[i] != "int" and self.entrada[i] != "float" ):                                    
                        print(f"Atribuição de valor invalido para a variável {self.codigo_real[pos_print]}, na linha {linha}")
                        return -1
                    else:
                        if (self.entrada[i] == "float" and self.tabela_simbolos["token"][pos] == "idInt"):
                            print(f"Atribuição de float para variavel inteira {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        else:
                            i=i+2

                elif(self.tabela_simbolos["token"][pos] == "idString"): # se é uma string
                    if (self.entrada[i] == "id"): # quem esta sendo atribuido é variavel
                        pos2 = self.procura_cod_tab_sim(self.codigo_real[i])

                        if(self.tabela_simbolos["token"][pos2] == "idInt" or self.tabela_simbolos["token"][pos2] == "idFloat"): # se o proximo a ser atribuido a ele é uma numerico
                            print(f"Atribuição de variavel numerica para variavel string {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                        elif(self.tabela_simbolos["token"][pos2] == "idBoolean"):
                            print(f"Atribuição de variavel boleana para variavel string {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                    elif(self.entrada[i] != "string"):                                    
                        print(f"Atribuição de valor invalido para a variável string {self.codigo_real[pos_print]}, na linha {linha}")
                        return -1
                    
                    else:
                            i=i+2

                elif(self.tabela_simbolos["token"][pos] == "idBoolean"): # se é um boolean
                    if (self.entrada[i] == "id"): # quem esta sendo atribuido é variavel
                        pos2 = self.procura_cod_tab_sim(self.codigo_real[i])

                        if(self.tabela_simbolos["token"][pos2] == "idInt" or self.tabela_simbolos["token"][pos2] == "idFloat"): # se o proximo a ser atribuido a ele é uma numerico
                            print(f"Atribuição de variavel numerica para variavel boleana {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                        elif(self.tabela_simbolos["token"][pos2] == "idString"):
                            print(f"Atribuição de variavel string para variavel boleana {self.codigo_real[pos_print]}, na linha {linha}")
                            return -1
                        
                    elif(self.codigo_real[i] != '0' and self.codigo_real[i] != '1'):                                    
                        print(f"Atribuição de valor invalido para a variavel boleana {self.codigo_real[pos_print]}, na linha {linha}")
                        return -1
                    
                    else:
                            i=i+2

                else:
                    i += 1
            return 0

    def read_file(self, file_name):
        with open(file_name, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            self.regras = list(leitor_csv) 

    def analise_sintatica(self):
        posi_entrada = 0
        controle = 1
        erro = 0
        self.tabela_simbolos = {
            "token":[],
            "cod":[],
            "utilizada":[]
        }
        self.tabela_laco = {
            "cod":[],
            "laco":[]
        }
        
        
        linha = 1
        laco = 0
        temp = 0 # Variavel utilizada para geracao de cod
        codAsString = "" # String para armazenar o cod gerado

        while controle < 1000:
            # print("----- Rodada ", controle, " -----")
            # print("Entrada ", self.entrada)
            # print("Pilha ", self.pilha, "\n\n")
            controle += 1

            pula_linha = True
            while(pula_linha == True):
                if(len(self.codigo_real) > 0 and self.codigo_real[0] == "\n"):
                    linha += 1
                    self.codigo_real.pop(0)
                else:
                    pula_linha = False
            
            if len(self.entrada) == 1 and len(self.pilha) == 1 and self.entrada[0] == self.pilha[-1] == '$':
                if erro > 0:
                    print("Aceito com", erro, "erros! ")

                else:
                    print("Aceito sem erros!")
                break

            topo = self.entrada[posi_entrada] if len(self.entrada) != 0 else "solucao"

            # print("Entrada -> ", self.entrada)
            # print("Cod real -> ", self.codigo_real, "\n")
            # print(self.tabela_simbolos)
            '''
            Entrada ->  ['for', 'id', 'atribuicao', 'int', 'virgula', 'id', 'op_relacional', 'int', 'virgula', 'id', 'incremento', 'col_esq', 'idInt', 'id', 'atribuicao', 'int', 'fim_linha', 'idInt', 'id', 'atribuicao', 'int', 'fim_linha', 'id', 'atribuicao', 'id', 'op_aritmetico', 'id', 'fim_linha', 'col_dir', 'fim_linha', '$']
            Cod real ->  ['for', 'i', ':=', '0', ',', 'i', '<', '20', ',', 'i', '++', '{', '\n', 'int', 'x', ':=', '2', ';', '\n', 'int', 'mult', ':=', '23', ';', '\n', 'x', ':=', 'x', '*', 'mult', ';', '\n', '}', ';', '\n', '\n', '\n']
            '''

            # Geracao de Cod.
            if(len(self.codigo_real) and self.codigo_real[0] != "ja_computado"): # Declara e ja atribui valor
                if(self.entrada[0] == "idInt" and self.entrada[2] == "atribuicao"):
                    codAsString += self.codigo_real[1] + ": " + "i32 = " + self.codigo_real[3] + "\n"

                if(self.entrada[0] == "idFloat" and self.entrada[2] == "atribuicao"):
                    codAsString += self.codigo_real[1] + ": " + "f64 = " + self.codigo_real[3] + "\n"

                if(self.entrada[0] == "idBoolean" and self.entrada[2] == "atribuicao"):
                    codAsString += self.codigo_real[1] + ": " + "bool = " + self.codigo_real[3] + "\n"

                if(self.entrada[0] == "idString" and self.entrada[2] == "atribuicao"):
                    codAsString += "Declaracao de string! ainda nao resolvida" + "\n"

                if(self.entrada[0] == "id"): # Atribuicao de valor
                    pos = self.procura_cod_tab_sim(self.codigo_real[0])
                    if(self.tabela_simbolos["token"][pos] == "idInt" and self.entrada[1] == "atribuicao"):
                        codAsString += self.codigo_real[0] + ": " + "i32 = " + self.codigo_real[2] + "\n"

                    if(self.tabela_simbolos["token"][pos] == "idFloat" and self.entrada[1] == "atribuicao"):
                        codAsString += self.codigo_real[0] + ": " + "f64 = " + self.codigo_real[2] + "\n"

                    if(self.tabela_simbolos["token"][pos] == "idBoolean" and self.entrada[1] == "atribuicao"):
                        codAsString += self.codigo_real[0] + ": " + "bool = " + self.codigo_real[2] + "\n"

                    if(self.tabela_simbolos["token"][pos] == "idString" and self.entrada[1] == "atribuicao"):
                        codAsString += "Declaracao de string! ainda nao resolvida" + "\n"

            # Semantico
            if(len(self.codigo_real) and self.codigo_real[0] != "ja_computado"): # Se ainda tem codigo e ele ainda nao foi computado
                if(self.entrada[0] == "idInt" or self.entrada[0] == "idFloat" or self.entrada[0] == "idBoolean" or self.entrada[0] == "idString"): # Se o codigo for uma declaracao
                    if(self.entrada[1] != "id"): # Se o proximo nao for um id = palavra reservada
                        print(f"Palavra {self.entrada[1]} reservada!, na linha {linha}")
                        erro += 1
                    elif(self.entrada[2] == "atribuicao" and (self.entrada[3] == "int" or self.entrada[3] == "string" or self.entrada[3] == "float" or self.entrada[3] == "id")):
                        if laco != 0:                           
                            self.append_tab_simbolo_laco(self.codigo_real[1],laco)
                        self.append_tab_simbolo(self.entrada[0], self.codigo_real[1], True) 

                        pos = self.procura_cod_tab_sim(self.codigo_real[1])
                        if (self.verifica_atribuicao(pos, linha, 3) == -1):
                            erro += 1
                        self.codigo_real[1] = "ja_computado" # Na declaracao, ja coloca esse ja_computado no cod do id, pra nao precisar analisar ele depois
                        self.codigo_real[0] = "ja_computado"

                    else:
                        if laco != 0:                             
                            self.append_tab_simbolo_laco(self.codigo_real[1],laco)
                        self.append_tab_simbolo(self.entrada[0], self.codigo_real[1], False)
                        self.codigo_real[1] = "ja_computado" # Na declaracao, ja coloca esse ja_computado no cod do id, pra nao precisar analisar ele depois
                        self.codigo_real[0] = "ja_computado"
                
                elif(self.entrada[0] == "col_dir"):   
                    if laco != 0: 
                            
                        for i in range(len(self.tabela_laco["laco"]) - 1, -1, -1):
                            if self.tabela_laco["laco"][i] == laco:
                                #print(self.tabela_laco["cod"][i])
                                self.tabela_simbolos["cod"].remove(self.tabela_laco["cod"][i])      
                                del self.tabela_laco["cod"][i]      
                                del self.tabela_laco["laco"][i]  
                        
                        laco = laco -1
 
                    self.codigo_real[0] = "ja_computado"
                    self.codigo_real[1] = "ja_computado"
                elif(self.entrada[0] == "for"):            
                    pos = self.procura_cod_tab_sim(self.codigo_real[1])
                    if(pos == -1):
                        print(f"Variavel {self.codigo_real[0]} nao declarada, na linha {linha}")
                        erro += 1
                        # print("TAB ", self.tabela_simbolos)
                    else:
                        self.tabela_simbolos["utilizada"][pos] = True
                        if (self.tabela_simbolos["token"][pos] != "idString" and self.tabela_simbolos["token"][pos] != "idBoolean"):
                            if (self.entrada[3] == "float" and self.tabela_simbolos["token"][pos] == "idInt"):
                                print(f"Atribuição de valor invalido para a variável {self.codigo_real[1]}, na linha {linha}")
                                erro += 1
                            else:
                                laco = laco + 1
                                self.codigo_real[1] = "ja_computado"                           
                    self.codigo_real[0] = "ja_computado"
                
                elif(self.entrada[0] == "id" and self.entrada[1] == "atribuicao"):
                    pos = self.procura_cod_tab_sim(self.codigo_real[0])
                    self.tabela_simbolos["utilizada"][pos] = True
                    if(pos == -1):
                        print(f"Variavel {self.codigo_real[0]} nao declarada, na linha {linha}")
                        erro += 1
                        # print("TAB ", self.tabela_simbolos)
                    else:
                        # if (self.tabela_simbolos["token"][pos] == "idBoolean"):
                        #     pos_valor_atribuido = self.procura_cod_tab_sim(self.codigo_real[2]) # Qual a posicao do valor a direita da atribuicao, usado para saber se os tipos batem
                        #     if(self.codigo_real[2] != '0' and self.codigo_real[2] != '1' and self.tabela_simbolos["token"][pos_valor_atribuido] != "idBoolean"):
                        #         print(f"Atribuição de valor invalido para a variável {self.codigo_real[0]}, na linha {linha}")
                        #         erro += 1
                        # else:
                        if(self.verifica_atribuicao(pos,linha,2) == -1):
                            erro += 1
                    self.codigo_real[0] = "ja_computado"

                elif(self.entrada[0] == "id" and self.entrada[1] != "atribuicao"):
                    pos = self.procura_cod_tab_sim(self.codigo_real[0])
                    if(pos == -1):
                        print(f"Variavel {self.codigo_real[0]} nao declarada, na linha {linha}")
                        erro += 1
                    elif(self.tabela_simbolos["utilizada"][pos] == False):

                        print(f"Variavel {self.codigo_real[0]} nao possui valor, na linha {linha}")
                        print("Entrada -> ", self.entrada)
                        print("Cod real -> ", self.codigo_real, "\n")
                        erro += 1
                    self.codigo_real[0] = "ja_computado"
                
            # Sintatico                           
            if len(self.pilha) > 0 and len(self.entrada) != 0 and self.entrada[posi_entrada] == self.pilha[-1]:
                # print("Desempilha ", self.pilha[-1], " avança na leitura da sentença")
                self.entrada.pop(0)
                self.codigo_real.pop(0)
                self.pilha.pop()
    
            elif len(self.pilha) > 0:
                producao = []
                for i in range(len(self.regras)):  
                    if self.regras[i][0] == self.pilha[-1]:
                        for j in range(len(self.regras[0])): 
                            if self.regras[0][j] == topo or topo == "solucao":                                
                                if self.regras[i][j] != '' and self.regras[i][j] != 'sinc':
                                    producao = self.regras[i][j].split(" ")
                                    producao_invertida = producao[::-1]
                                    self.pilha.pop()
                                    if producao_invertida != ['<Vazio>']:
                                        self.pilha.extend(producao_invertida)
                                    # print("Empilha: ", producao_invertida) 
                                    # print("Pilha total", self.pilha, "\n\n")
                                
                                elif self.regras[i][j] == '':
                                    # print("Entrada da tabela vazia")
                                    if len(self.pilha) > 1:
                                        # print("Descartando o Token", self.entrada[0], "\n\n")                                    
                                        self.entrada.pop(0)
                                        self.codigo_real.pop(0)
                                        erro += 1
                                        
                                else:
                                    # print("Entrada Sinc")
                                    if len(self.pilha) > 0 and self.pilha[-1] != '$':
                                        self.pilha.pop()
                                    # print(self.entrada)
                                    erro += 1
                if not self.pilha:
                    # print("Erro: Pilha vazia. A análise foi interrompida.")
                    break

        if(erro == 0):
                with open("cod.txt", "w") as file:
                    file.write(codAsString)

my_lex = Automato()  
my_lex.read_file("cod_teste3.txt")
my_lex.analyzes_code()

tokens_solo = [i[1] for i in my_lex.tokens if i[1] != "ContraBarraN" and i[1] != "comentario"]
real_code = [i[0] for i in my_lex.tokens if "@" not in i[0]]

# print("Real code ", real_code)

sintatico = Sintatico(tokens_solo, real_code)
