def knapSack(peso_max, itens, n, it=[]):
	if n == 0:
		return [0, it]

	if (itens[n-1]['peso'] > peso_max):
		return knapSack(peso_max, itens, n-1, it)
 
	else:
		recComItem = knapSack(peso_max-itens[n-1]['peso'], itens, n-1)
		reqSemItem = knapSack(peso_max, itens, n-1)
		pesoComItem = itens[n-1]['valor'] + recComItem[0]
		pesoSemItem = reqSemItem[0]

		peso = max(pesoComItem, pesoSemItem)

		if peso == pesoComItem:
			c = [itens[n-1], *recComItem[1]]
		else:
			c = [*reqSemItem[1]]

		return [peso, c]



itens = [
	{'id': 1, 'peso': 12, 'valor': 60}, 
	{'id': 2, 'peso': 30, 'valor': 250}, 
	{'id': 3, 'peso': 20, 'valor': 120},
	{'id': 4, 'peso': 25, 'valor': 200},
	{'id': 5, 'peso': 80, 'valor': 270},
]

peso_max = 90
num = len(itens)
print(knapSack(peso_max, itens, num))
 