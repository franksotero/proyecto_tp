lista1 = []
for i in range(3):
    lista1.append(0)
print(lista1)

lista2 = [0 for i in range(3)]
print(lista2)

matriz = [[0 for i in range(4)] for i in range(3)]
print(matriz)

pares = [i for i in range(10) if i % 2 == 0]
print(pares)

pares2 = [i if i % 2 == 0 else -1 for i in range(10)]
print(pares2)
