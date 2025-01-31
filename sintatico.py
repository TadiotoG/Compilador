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
        
        linha = 1

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

            # Semantico
            if(len(self.codigo_real) and self.codigo_real[0] != "ja_computado"):
                if(self.entrada[0] == "idInt" or self.entrada[0] == "idFloat" or self.entrada[0] == "idBoolean" or self.entrada[0] == "idString"):
                    if(self.entrada[1] != "id"):
                        print(f"Palavra {self.entrada[1]} reservada!, na linha {linha}")
                        erro += 1
                    elif(self.entrada[2] == "atribuicao" and (self.entrada[3] == "int" or self.entrada[3] == "string" or self.entrada[3] == "float" or self.entrada[3] == "id")):
                        self.append_tab_simbolo(self.entrada[1], self.codigo_real[1], True)
                        self.codigo_real[1] = "ja_computado" # Na declaracao, ja coloca esse ja_computado no cod do id, pra nao precisar analisar ele depois
                    else:
                        self.append_tab_simbolo(self.entrada[1], self.codigo_real[1], False)
                        self.codigo_real[1] = "ja_computado" # Na declaracao, ja coloca esse ja_computado no cod do id, pra nao precisar analisar ele depois

                elif(self.entrada[0] == "id" and self.entrada[1] == "atribuicao"):
                    pos = self.procura_cod_tab_sim(self.codigo_real[0])
                    if(pos == -1):
                        print(f"Variavel {self.codigo_real[0]} nao declarada, na linha {linha}")
                        erro += 1
                        # print("TAB ", self.tabela_simbolos)
                    else:
                        self.tabela_simbolos["utilizada"][pos] = True
                    self.codigo_real[0] = "ja_computado"

                elif(self.entrada[0] == "id" and self.entrada[1] != "atribuicao"):
                    pos = self.procura_cod_tab_sim(self.codigo_real[0])
                    if(pos == -1):
                        print(f"Variavel {self.codigo_real[0]} nao declarada, na linha {linha}")
                        erro += 1
                    elif(self.tabela_simbolos["utilizada"][pos] == False):
                        print(f"Variavel {self.codigo_real[0]} nao possui valor, na linha {linha}")
                        erro += 1
                    self.codigo_real[0] = "ja_computado"
            

                           
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
                                    print("Entrada da tabela vazia")
                                    if len(self.pilha) > 1:
                                        print("Descartando o Token", self.entrada[0], "\n\n")                                    
                                        self.entrada.pop(0)
                                        self.codigo_real.pop(0)
                                        erro += 1
                                        
                                else:
                                    print("Entrada Sinc")
                                    if len(self.pilha) > 0 and self.pilha[-1] != '$':
                                        self.pilha.pop()
                                    print(self.entrada)
                                    erro += 1
                if not self.pilha:
                    print("Erro: Pilha vazia. A análise foi interrompida.")
                    break
        
my_lex = Automato()  
my_lex.read_file("cod_teste3.txt")
my_lex.analyzes_code()

tokens_solo = [i[1] for i in my_lex.tokens if i[1] != "ContraBarraN" and i[1] != "comentario"]
real_code = [i[0] for i in my_lex.tokens if "@" not in i[0]]

# print("Real code ", real_code)

sintatico = Sintatico(tokens_solo, real_code)
