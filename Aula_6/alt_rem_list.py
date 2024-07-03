motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

#alterando o valor da posição 1
motorcycles[0] = 'Ducati'
print(motorcycles)

del motorcycles[0]
print(motorcycles)


#criando uma variável "popped_motorcycle" e passamos o valor de pop
#retirando o último item da lista
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#repetindo a ação
one_more_popped = motorcycles.pop()
print(one_more_popped)