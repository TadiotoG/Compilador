import csv

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
        controle = 0
        while controle < 10:
            controle += 1
            #if len(self.entrada) == 0 :
             #   print("Aceita")
              #  break  

            topo = self.entrada[posi_entrada]
            posi = len(self.pilha) - 1
            producao = []
            #print("Entrada", self.entrada)
            #print("Pilha", self.pilha)
                
            if self.entrada[posi_entrada] == self.pilha[posi]:
                print("Desempilha", self.pilha[posi], "avança na leitura da sentença")
                self.entrada.pop(0)
                self.pilha.pop(posi)
            else:
                
                for i in range(len(self.regras)):  
                    if self.regras[i][0] == self.pilha[posi]:
                        for j in range(len(self.regras[0])): 
                            
                            if self.regras[0][j] == topo:
                                
                                print("Entrada",topo)
                                print("Pilha", self.pilha[posi])
                                print(i , j)
                                print(self.regras[i][j+1])
                                if self.regras[i][j] != '':
                                    
                                    print(self.regras[i][j])
                                    producao = self.regras[i][j]  
                                    producao = producao.split(" ")  
                                    producao_invertida = producao[::-1]
                                    self.pilha.pop(0)  
                                    self.pilha.extend(producao_invertida) 
                                