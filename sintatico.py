import csv
from lexico import Automato

class Sintatico:
    def __init__(self, tokens):
        self.entrada = tokens
        self.pilha = []
        self.regras = []
        self.pilha.append('<program>')
        self.read_file('Tabela_Regras.csv')
        self.analise_sintatica()
        
    def read_file(self, file_name):
        with open(file_name, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            self.regras = list(leitor_csv) 

    def analise_sintatica(self):
        posi_entrada = 0
        controle = 1
        while controle < 50:
            print("----- Rodada ", controle, " -----")
            controle += 1
            if len(self.entrada) == 0 :
                print("Aceita")
                break  

            topo = self.entrada[posi_entrada]
                           
            if self.entrada[posi_entrada] == self.pilha[-1]:
                print("Desempilha ", self.pilha[-1], " avança na leitura da sentença")
                self.entrada.pop(0)
                self.pilha.pop()
                print("Pilha total", self.pilha, "\n\n")
            else:
                producao = []
                for i in range(len(self.regras)):  
                    #print("Verificando", self.regras[i][0] , self.pilha[posi])
                    if self.regras[i][0] == self.pilha[-1]:
                        #print("Entrou", self.regras[i][0] , self.pilha[posi])
                        for j in range(len(self.regras[0])): 
                            
                            if self.regras[0][j] == topo:
                                
                                print("Entrada", topo)
                                print("Pilha[", len(self.pilha)-1, "]:", self.pilha[-1])
                                print(i , j)
                                #print(self.regras[i][j+1])
                                if self.regras[i][j] != '':
                                    
                                    print(self.regras[i][j])
                                    producao = self.regras[i][j]  
                                    producao = producao.split(" ")  
                                    producao_invertida = producao[::-1]
                                    self.pilha.pop()
                                    self.pilha.extend(producao_invertida)
                                    print("Empilha: ", producao_invertida) 
                                    print("Pilha total", self.pilha, "\n\n")
                    
my_lex = Automato()  

my_lex.read_file("cod_teste2.txt")
my_lex.analyzes_code()

tokens_solo = []
for i in my_lex.tokens:
    if (i[1] != 'ContraBarraN' and i[1] != "comentario"):
        tokens_solo.append(i[1])
print("Tokens: ", tokens_solo)

sintatico = Sintatico(tokens_solo)