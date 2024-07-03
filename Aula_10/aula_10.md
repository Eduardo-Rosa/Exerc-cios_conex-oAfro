# Programação Orientada a Objetos

## Classes e objetos

Classes e objetos são conceitos fundamentais na programação orientada a objetos, permitindo a criação de estruturas organizadas e reutilizáveis em Python. Ao entender esses conceitos, os desenvolvedores podem criar sistemas mais flexíveis e escaláveis.
## Classes:
    - Uma classe é um construtor de objetos ou um "modelo" para criar objetos.
    - Os objetos são apenas uma encapsulação de variáveis e funções em uma única entidade.
    - Os objetos obtêm suas variáveis e funções das classes.
    - Para criar uma classe, usamos a palavra-chave class.
    - A primeira string dentro da classe é chamada de docstring, que fornece uma breve descrição sobre a classe.
    - Todas as classes têm uma função chamada de init(), que é sempre executada quando a classe é iniciada.
    - Para atribuir valores às propriedades do objeto ou outras operações necessárias ao criar o objeto.
    - O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis de classe. 
    - self deve ser o primeiro parâmetro de qualquer função na classe.
    - A função embutida super() retorna um objeto temporário da superclasse que nos permite acessar métodos da classe base. super() nos permite evitar usar explicitamente o nome da classe base e habilitar a herança múltipla.

### Explicação 1 :

Se as entradas do usuário variarem, digamos de 1 a 100. E o compilador selecionou aleatoriamente 42 como o número inteiro. 

E agora o jogo de adivinhação começou, então o usuário digitou 50 como seu primeiro palpite . 

O compilador mostra “Tente novamente! Você adivinhou alto demais”. Isso significa que o número aleatório (ou seja, 42) não está no intervalo de 50 a 100. Essa é a importância de adivinhar metade do intervalo. 
 
E novamente, o usuário adivinha metade de 50 (você poderia me dizer por quê?). Portanto, a metade de 50 é 25. O usuário insere 25 como sua segunda estimativa . Desta vez, o compilador mostrará: “Tente novamente! Você adivinhou muito pequeno”. Isso significa que os números inteiros menores que 25 (de 1 a 25) são inúteis para serem adivinhados. 
 
Agora o intervalo de adivinhação do usuário é menor, ou seja, de 25 a 50. De forma inteligente! O usuário adivinhou metade desse intervalo, de modo que o usuário adivinhou 37 como seu terceiro palpite .
 
Desta vez, novamente o compilador mostra a saída “Tente novamente! Você adivinhou muito pequeno”. Para o usuário, o intervalo de adivinhação está diminuindo a cada tentativa. Agora, o intervalo de adivinhação do usuário é de 37 a 50, para o qual o usuário adivinhou 43 como sua quarta estimativa .

Desta vez, o compilador mostrará uma saída “Tente novamente! Você adivinhou alto demais”. Assim, o novo intervalo de adivinhação para os usuários será de 37 a 43, novamente para o qual o usuário adivinhou a metade desse intervalo, ou seja, 40 como seu quinto palpite . Desta vez, o compilador mostra a saída “Tente novamente! Você adivinhou muito pequeno”. Deixando o palpite ainda menor, de 41 a 43. E agora o usuário adivinhou 41 como seu sexto palpite .

O que está errado e mostra a saída “Tente novamente! Você adivinhou muito pequeno”. E, finalmente, o usuário adivinhou o número certo, que é 42, como seu sétimo palpite .