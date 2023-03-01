# String Validation Using Automata - DFA, NFA and NFAe

## README - Autômato validador de palavras

Este arquivo é uma interface para o arquivo automata.py, que é o arquivo principal do projeto. O arquivo automata.py é responsável por ler o arquivo e criar o autômato, e o arquivo main.py é responsável por ler a entrada e chamar o autômato para verificar se a palavra é aceita ou não.

Requisitos:

- Interpretador Python 3.10.6
  
Como executar:

1. Baixe todos os arquivos do projeto em um diretório local.

2. Abra o terminal na pasta onde os arquivos foram salvos.

3. Execute o seguinte comando no terminal:

    

    ```Python
    python main.py
    ```

4. Escolha a opção 1 do menu para ler o autômato de um arquivo.

5. Insira o nome do arquivo (com extensão) localizado na pasta inputs.

6. Insira o nome do arquivo de strings (com extensão) localizado na pasta strings.

7. O programa irá validar cada palavra do arquivo de strings e exibir se é aceita ou não pelo autômato.

8. O resultado de cada palavra será salvo em um arquivo de saída localizado na pasta outputs.

Observações:

Os arquivos de entrada devem estar nas pastas inputs e strings.
Os arquivos de saída serão salvos na pasta outputs.
Caso o arquivo de saída já exista, o resultado da nova execução será adicionado ao final do arquivo.
