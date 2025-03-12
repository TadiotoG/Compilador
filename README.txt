# Analisador Semântico

![GitHub](https://img.shields.io/badge/Projeto-Compiladores-blue)

## 📌 Universidade Estadual do Oeste do Paraná  
**Centro de Ciências Exatas e Tecnológicas**  
**Colegiado de Ciência da Computação**  

### 📌 Disciplina: Compiladores - Parte 3
**Alunos:**  
- David Antonio Brocardo  
- Gabriel Tadioto de Oliveira  

**📅 Data:** 30/01/2025

---

## 📌 Introdução
Este projeto implementa um **Analisador Semântico**, a terceira parte de um compilador. O objetivo principal é verificar a coerência semântica do código-fonte, assegurando a correta declaração e uso de variáveis, compatibilidade de tipos, regras de escopo e integridade da tabela de símbolos.

## 🚀 Entrada
O Analisador Semântico recebe como entrada uma lista de tokens extraídos do código-fonte, representados da seguinte forma:

```python
['idFloat', 'id', 'fim_linha', 'idString', 'id', 'fim_linha', 'idBoolean', 'id', 'fim_linha', 
'idInt', 'id', 'fim_linha', 'id', 'atribuicao', 'id', 'fim_linha', 'for', 'id', 'atribuicao', 
'int', 'virgula', 'id', 'op_relacional', 'id', 'virgula', 'id', 'incremento', 'col_esq', 'id', 
'atribuicao', 'id', 'op_aritmetico', 'id', 'fim_linha', 'col_dir', 'fim_linha', '$']
```

## ⚙️ Funcionalidades
### ✅ Declaração prévia de variáveis
O analisador verifica se as variáveis foram declaradas antes do uso. Os tipos suportados são:

- **Float:** `idFloat id`
- **String:** `idString id`
- **Boolean:** `idBoolean id`
- **Int:** `idInt id`

### ✅ Verificação de escopo
Assegura que cada identificador pertence a um escopo válido.

### ✅ Unicidade dos identificadores
Garante que cada identificador seja único dentro do seu escopo.

### ✅ Uso de variáveis
Verifica se todas as variáveis declaradas foram utilizadas no programa.

### ✅ Sistema de Tipos
Realiza a verificação de compatibilidade entre tipos nas operações matemáticas:

- **Válido:**
  - `Float = Float + int`
  - `Float = Float + Float`
  - `Int = Int + Int`
- **Inválido:**
  - Operar com tipos `Boolean` e `String` em expressões aritméticas.

---

## 📑 Tabela de Símbolos
A Tabela de Símbolos é uma estrutura essencial do Analisador Semântico. Suas funções incluem:

- **Armazenamento incremental:** informações são coletadas durante a análise e usadas na geração do código objeto.
- **Pesquisa e alteração dinâmica:** a tabela é consultada cada vez que um identificador é encontrado, e novas informações são adicionadas conforme necessário.

### 📌 Estrutura da Tabela de Símbolos
Cada entrada na tabela de símbolos contém:
- **Nome ou lexema** (identificador da variável ou procedimento)
- **Tipo** (Float, Int, Boolean, String)
- **Escopo** (definição de onde a variável pode ser acessada)

### 📌 Principais Operações
- **🔹 Inserir:** Armazena informações das declarações.
- **🔹 Verificar (lookup):** Recupera informação associada a um identificador quando ele é utilizado.
- **🔹 Remover:** Exclui informações de um identificador quando ele não é mais necessário.

---

## 🎯 Conclusão
Este analisador semântico assegura que o programa está semanticamente correto antes da geração do código objeto. Ele verifica a declaração de variáveis, a coerência dos tipos e o escopo dos identificadores, garantindo uma compilação bem-sucedida.

---

## 📌 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o analisador:
   ```bash
   python analisador_semantico.py
   ```

---

## 🛠️ Tecnologias Utilizadas
- Python 🐍
- Algoritmos de Compiladores
- Análise Semântica

---

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

**Desenvolvido por:**  
David Antonio Brocardo e Gabriel Tadioto de Oliveira 🚀

