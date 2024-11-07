import csv
from lexico import Automato

class Sintatico:
    def __init__(self, tokens):
        self.entrada = tokens
        self.pilha = []
        self.regras = []
        self.pilha.append('<program>')
        self.read_file('Tabela_Regras2.csv')
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
            print(self.entrada)
            controle += 1
            if (len(self.entrada) == 0 and len(self.pilha) == 0):
                print("Aceita")
                break  

            if len(self.entrada) != 0:
                topo = self.entrada[posi_entrada]

            else:
                topo = "gambiarra"
                           
            if len(self.entrada) != 0 and self.entrada[posi_entrada] == self.pilha[-1]:
                print("Desempilha ", self.pilha[-1], " avança na leitura da sentença")
                print("Pilha Antes", self.pilha, "\n\n")
                self.entrada.pop(0)
                self.pilha.pop()
                print("Pilha total", self.pilha, "\n\n")
            else:
                producao = []
                for i in range(len(self.regras)):  
                    if self.regras[i][0] == self.pilha[-1]:
                        #print("Verificando", self.regras[i][0] , self.pilha[-1])
                        #print("Pilha total", self.pilha, "\n\n") 
                        #print("Entrada total", self.entrada,"\n\n")                      
                        for j in range(len(self.regras[0])): 
                            #print("Verificando", self.regras[0][j] , topo)
                            if self.regras[0][j] == topo or topo == "gambiarra":
                                
                                print("Entrada", topo, " gostaria de saber:", len(self.pilha))
                                print("Pilha[", len(self.pilha)-1, "]:", self.pilha[-1])
                                print(i , j)
                                print(self.regras[i][j])
                                if self.regras[i][j] != '' and self.regras[i][j] != 'sinc':

                                    #print(self.regras[i][j])
                                    producao = self.regras[i][j]  
                                    producao = producao.split(" ")  
                                    producao_invertida = producao[::-1]
                                    self.pilha.pop()
                                    teste = ['<Vazio>']
                                    if producao_invertida != ['<Vazio>']:
                                        self.pilha.extend(producao_invertida)
                                    print("Empilha: ", producao_invertida) 
                                    print("Pilha total", self.pilha, "\n\n")
                                elif self.regras[i][j] != '':
                                    print("Entrada da tabela vazia")
                                    print("Descartando o Token", self.entrada[0], "\n\n")
                                    self.entrada.pop(0)

                                else:
                                    print("Entrada Sinc")
                                    print("Descartando o Não terminal ", self.pilha[-1], " da pilha \n\n")
                                    self.pilha.pop()


my_lex = Automato()  

my_lex.read_file("cod_teste3.txt")
my_lex.analyzes_code()

tokens_solo = []

for i in my_lex.tokens:
    if (i[1] != "ContraBarraN" and i[1] != "comentario"):        
        tokens_solo.append(i[1])
print("Tokens: ", tokens_solo)

sintatico = Sintatico(tokens_solo)