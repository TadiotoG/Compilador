                                    INSTRUÇÕES DE USO

Para compilar e executar o analisador léxico, deverá utilizar uma IDE que suporte códigos em Python, 
bem como ter o Python instalado devidamente em sua máquina 

Caso tenha o Python devidamente instalado em sua máquina, realize os seguintes passos:

    1. Acesse o Windows PowerShell ou Terminal do Linux, no diretório ao qual os programas estão salvos
    2. Para executar, realize o seguinte comando :
        ->  python lexico.py   
                    ou  
        ->  python3 nome_do_arquivo.py


- Caso deseje alterar o arquivo de entrada no analisador léxico, deverá realizar o seguintes passos:
    1. Navegue até o final do código
    2. Localize o seguinte trecho de código:
        "my_lex.read_file("exemplo.txt")"
    3. Altere para o arquivo desejado.


_ tokens juntos é correto 12A

- salva linha junto com tokens
- ++  e  -- reconhecer juntos
- tratamento da string abra e fecha " "
- int -> id tipo int
- indentificar as palavras reservadas.


