# Estrutura de Repetição while

O laço de repetição while permite executar um bloco de código repetidamente enquanto uma condição for verdadeira. 
 ex:
 while condição:
     bloco de código a ser repetido

A condição é avaliada antes de cada iteração e, se for verdadeira, o bloco de código é executado. Caso contrário, o laço é encerrado.

## Boas Práticas
    - **Evitar Loops Infinitos:** Certifique-se de que a condição do while eventualmente se torne falsa.
    - **Controle de Fluxo:** Utilize break e continue para um controle mais fino do fluxo do laço.
    - **Clareza do Código:** Mantenha a lógica do laço clara e simples para facilitar a manutenção e compreensão do código.

## Exercicio em Sala

### Exercício 1

Neste exercício, você irá implementar um laço de repetição while para criar uma contagem regressiva a partir de um número fornecido pelo usuário. A entrada do usuário deve ser validada para garantir que é um número inteiro positivo.

    1 - Solicite um número ao usuário e verifique se a entrada é válida.
    2 - Utilize um laço while para realizar a contagem regressiva a partir do número fornecido até zero.
    3 - Imprima cada número da contagem no console.

## Exercício 2

Neste exercício, você irá criar uma calculadora interativa que soma números fornecidos pelo usuário até que um número negativo seja inserido. Quando um número negativo for inserido, a calculadora exibirá o total da soma e encerrará.

    1 - Inicialize a soma com o valor 0.
    2 - Solicite números ao usuário continuamente até que um número negativo seja inserido.
    3 - Adicione cada número positivo à soma.
    4 - Encerre o loop quando um número negativo for inserido e exiba a soma total.