# Lista


## O que é uma lista?

As listas são estruturas de dados fundamentais em Python, permitindo armazenar e manipular coleções de elementos de forma eficiente. Elas são amplamente utilizadas em programação para diversas finalidades, como armazenar dados, iterar sobre elementos e realizar operações de filtragem e transformação.

Uma lista é uma coleção de itens em uma ordem específica. 

Você pode criar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os nomes de todas as pessoas da sua família. 

Você pode colocar qualquer coisa que desejar em uma lista, e os itens na sua lista não precisam estar relacionados de forma particular. Como uma lista geralmente contém mais de um elemento, é uma boa ideia fazer o nome da sua lista no plural, como letras, dígitos ou nomes. 

Em Python, colchetes quadrados ([]) indicam uma lista, e os elementos individuais na lista são separados por vírgulas. Aqui está um exemplo simples de uma lista que contém alguns tipos de bicicletas:
Ex == **modelo_lst_1.py**

## Acessando Elementos em uma Lista

Listas são coleções ordenadas, então você pode acessar qualquer elemento em uma lista informando ao Python a posição, ou índice, do item desejado. 

Para acessar um elemento em uma lista, escreva o nome da lista seguido pelo índice do item entre colchetes. Por exemplo, vamos acessar a primeira bicicleta na lista bicicletas:
ex == acess_lst.py

## Formatando saida em uma lista

Este é o resultado que você deseja que seus usuários vejam — saída limpa e formatada de maneira organizada. Você também pode usar os métodos de string em qualquer elemento em uma lista. Por exemplo, você pode formatar o elemento 'trek' de maneira mais organizada usando o método title():

ex: **format_list.py**


## Alterando, Adicionando e Removendo Elementos
Este trecho destaca a dinamicidade das listas em Python, permitindo a adição, remoção e modificação de elementos conforme necessário durante a execução do programa.

A maioria das listas que você criar será dinâmica, o que significa que você construirá uma lista e então adicionará e removerá elementos conforme seu programa é executado. Por exemplo, você pode criar um jogo no qual um jogador precisa atirar em aliens que estão no céu. Você poderia armazenar o conjunto inicial de aliens em uma lista e então remover um alien da lista cada vez que um for abatido.

Cada vez que um novo alien aparecer na tela, você o adiciona à lista. Sua lista de aliens diminuirá e aumentará de tamanho ao longo do jogo. Modificando Elementos em uma Lista A sintaxe para modificar um elemento é similar à sintaxe para acessar um elemento em uma lista. Para alterar um elemento, use o nome da lista seguido pelo índice do elemento que você deseja alterar e, em seguida, forneça o novo valor que deseja que esse item tenha.

Ex: **alt_rem_list.py**


## Adicionando Elementos a uma Lista
Você pode querer adicionar um novo elemento a uma lista por muitas razões. Por exemplo, você pode querer fazer novos aliens aparecerem em um jogo, adicionar novos dados a uma visualização ou adicionar novos usuários registrados a um site que você construiu. Python oferece várias maneiras de adicionar novos dados a listas existentes.

## Anexando Elementos ao Final de uma Lista
A maneira mais simples de adicionar um novo elemento a uma lista é anexar o item à lista. Quando você anexa um item a uma lista, o novo elemento é adicionado ao final da lista. Usando a mesma lista que tínhamos no exemplo anterior, vamos adicionar o novo elemento 'ducati' ao final da lista.

ex: **add_list.py**

## Removendo Elementos de uma Lista
Frequentemente, você vai querer remover um item ou um conjunto de itens de uma lista. Por exemplo, quando um jogador derruba um alienígena do céu, provavelmente vai querer removê-lo da lista de alienígenas ativos. Ou quando um usuário decide cancelar sua conta em um aplicativo web que você criou, você vai querer remover esse usuário da lista de usuários ativos.

Você pode remover um item de acordo com sua posição na lista ou de acordo com seu valor. Removendo um Item Usando a Declaração del Se você conhece a posição do item que deseja remover de uma lista, pode usar a declaração **del**.

ex: **alt_rem_list.py**


## Removendo um Item Usando o Método pop()
O método pop() em Python remove o último item de uma lista e retorna esse item para que você possa manipulá-lo posteriormente. É útil quando você precisa acessar o último elemento de uma lista enquanto o remove.

Às vezes, você desejará usar o valor de um item após removê-lo de uma lista. Por exemplo, pode querer obter a posição x e y de um alienígena que acabou de ser abatido, para desenhar uma explosão nessa posição. Em uma aplicação web, você pode querer remover um usuário de uma lista de membros ativos e, em seguida, adicioná-lo a uma lista de membros inativos. O método **pop()** remove o último item de uma lista, mas permite que você trabalhe com esse item após removê-lo. O termo "pop" vem da ideia de pensar em uma lista como uma pilha de itens e retirar um item do topo da pilha. Nessa analogia, o topo de uma pilha corresponde ao final de uma lista.

ex: **alt_rem_list.py**


## Removendo Itens de Qualquer Posição em uma Lista

Na verdade, você pode usar o método pop() para remover um item em uma lista em qualquer posição, incluindo o índice do item que deseja remover entre parênteses.

Lembre-se de que cada vez que você usa pop(), o item com o qual está trabalhando não está mais armazenado na lista.

Se você não tem certeza se deve usar a instrução del ou o método pop(), aqui está uma maneira simples de decidir: quando você deseja excluir um item de uma lista e não usar esse item de forma alguma, use a instrução del; se você deseja usar um item conforme o remove, use o método pop().

ex: **lst_clientes.py**


## Removendo um Item pelo Valor
Às vezes, você não saberá a posição do valor que deseja remover de uma lista. Se você apenas conhece o valor do item que deseja remover, pode usar o método remove().

ex: **lst_clientes.py**