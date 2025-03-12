![Unioeste](Imagens/logo_unioeste.png)

# Analisador Semântico e Gerador de Código Intermediário

**Universidade Estadual do Oeste do Paraná**  
**Centro de Ciências Exatas e Tecnológicas**  
**Colegiado de Ciência da Computação**  

## Disciplina: Compiladores
**Alunos:**  
- **David Antonio Brocardo**  
- **Gabriel Tadioto de Oliveira**  



---

## Introdução

Este projeto implementa um **Compilador** , abrangendo todas as etapas do processo de compilação: Análise Léxica, Sintática, Semântica e Geração de Código. O objetivo principal é garantir a correta tradução do código-fonte.

## Analisador Semântico
Verificando a coerência semântica, assegurando a correta declaração e uso de variáveis, compatibilidade de tipos, regras de escopo. integridade da tabela de símbolos e a geração eficiente do código final.

## Entrada
O Analisador Semântico recebe como entrada uma lista de tokens extraídos do código-fonte, representados da seguinte forma:

```
['idFloat', 'id', 'fim_linha', 'idString', 'id', 'fim_linha', 'idBoolean', 'id', 'fim_linha', 
'idInt', 'id', 'fim_linha', 'id', 'atribuicao', 'id', 'fim_linha', 'for', 'id', 'atribuicao', 
'int', 'virgula', 'id', 'op_relacional', 'id', 'virgula', 'id', 'incremento', 'col_esq', 'id', 
'atribuicao', 'id', 'op_aritmetico', 'id', 'fim_linha', 'col_dir', 'fim_linha', '$']
```

## Funcionalidades
### **Declaração prévia de variáveis**
O analisador verifica se as variáveis foram declaradas antes do uso. Os tipos suportados são:

- **Float:** `idFloat id`
- **String:** `idString id`
- **Boolean:** `idBoolean id`
- **Int:** `idInt id`

### **Verificação de escopo**
Assegura que cada identificador pertence a um escopo válido.

### **Unicidade dos identificadores**
Garante que cada identificador seja único dentro do seu escopo.

### **Uso de variáveis**
Verifica se todas as variáveis declaradas foram utilizadas no programa.

### **Verificação de Laços**
Garante que as váriaveis declaradas dentro de laços e condicionais, sejam válidas somente dentro de seu escopo.

### **Sistema de Tipos**
Realiza a verificação de compatibilidade entre tipos nas operações matemáticas:

- **Válido:**
  - `Float = Float + int`
  - `Float = Float + Float`
  - `Int = Int + Int`
- **Inválido:**
  - Operar com tipos `Boolean` e `String` em expressões aritméticas.

---

## Tabela de Símbolos
A Tabela de Símbolos é uma estrutura essencial do Analisador Semântico. Suas funções incluem:

- **Armazenamento incremental:** informações são coletadas durante a análise e usadas na geração do código objeto.
- **Pesquisa e alteração dinâmica:** a tabela é consultada cada vez que um identificador é encontrado, e novas informações são adicionadas conforme necessário.

### **Estrutura da Tabela de Símbolos**
Cada entrada na tabela de símbolos contém:
- **Nome ou lexema (Token)** (identificador da variável ou procedimento)
- **Código Real** (Código real que o token representa)
- **Utilizada** (Verificando se a váriavel já foi utilizada)


---

## Gerador de Código Intermediário
O Gerador de Código Intermediário deste compilador traduz a representação semântica do código-fonte para a linguagem Extend Three Address Code (ETAC).  Essa etapa tem como objetivo otimizar a transição entre a análise semântica e a geração de código final, garantindo a correta estruturação das operações, alocação de temporários.

### Exemplo de uso
- **Código Original**           
-`int i := 0;`                    
-`for i := 0, i < pot, i++ {`      
-` x := x * mult;`                
-`};`                               
- **Código Intermediário**                                 
-`i: i32 = (i32)0`                                
-`loop0: `  
-` t1 : i32 = t1 + 1`   
-` t2 : bool = t1 < pot`  
-` t3: f64 = (f64)x * (f64)mult`  
-` x = t3`      
-`IF t2 goto loop0`                     
---


## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/TadiotoG/Compilador.git 
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd Compilador
   ```
3. Execute o analisador:
   ```bash
   python compilador.py
   ```

---

## Tecnologias Utilizadas
- **Python**



