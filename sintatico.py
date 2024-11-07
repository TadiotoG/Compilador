# Aluno: Gabriel Tadioto Oliveira e David Antonio Brocardo
# Trabalho de Compiladores - 2

import csv
from lexico import Automato

class Sintatico:
    def __init__(self, tokens):
        self.entrada = tokens
        self.pilha = []
        self.regras = []
        self.pilha.append('$')
        self.entrada.append('$')
        self.pilha.append('<program>')
        self.read_file('Tabela_Regras.csv')
        self.analise_sintatica()
        self.erro = 0
        
    def read_file(self, file_name):
        with open(file_name, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            self.regras = list(leitor_csv) 

    def analise_sintatica(self):
        posi_entrada = 0
        controle = 1
        erro = 0
        while controle > 0:
            print("----- Rodada ", controle, " -----")
            print("Entrada ", self.entrada)
            print("Pilha ", self.pilha, "\n\n")
            controle += 1
            
            if len(self.entrada) == 1 and len(self.pilha) == 1 and self.entrada[0] == self.pilha[-1] == '$':
                if erro > 1:
                    print("Aceito com erros!")

                else:
                    print("Aceito!")
                break

            topo = self.entrada[posi_entrada] if len(self.entrada) != 0 else "gambiarra"
                           
            if len(self.pilha) > 0 and len(self.entrada) != 0 and self.entrada[posi_entrada] == self.pilha[-1]:
                print("Desempilha ", self.pilha[-1], " avança na leitura da sentença")
                self.entrada.pop(0)
                self.pilha.pop()
    
            elif len(self.pilha) > 0:
                producao = []
                for i in range(len(self.regras)):  
                    if self.regras[i][0] == self.pilha[-1]:
                        for j in range(len(self.regras[0])): 
                            if self.regras[0][j] == topo or topo == "gambiarra":                                
                                if self.regras[i][j] != '' and self.regras[i][j] != 'sinc':
                                    producao = self.regras[i][j].split(" ")
                                    producao_invertida = producao[::-1]
                                    self.pilha.pop()
                                    if producao_invertida != ['<Vazio>']:
                                        self.pilha.extend(producao_invertida)
                                    print("Empilha: ", producao_invertida) 
                                    print("Pilha total", self.pilha, "\n\n")
                                
                                elif self.regras[i][j] == '':
                                    print("Entrada da tabela vazia")
                                    if len(self.pilha) > 1:
                                        print("Descartando o Token", self.entrada[0], "\n\n")                                    
                                        self.entrada.pop(0)
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
my_lex.read_file("cod_teste2.txt")
my_lex.analyzes_code()

tokens_solo = [i[1] for i in my_lex.tokens if i[1] != "ContraBarraN" and i[1] != "comentario"]

sintatico = Sintatico(tokens_solo)
