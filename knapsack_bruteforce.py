def knapSack(peso_max, itens, n, it=[]):
	if n == 0:
		return [0, it]

	if (itens[n-1]['peso'] > peso_max):
		return knapSack(peso_max, itens, n-1, it)
 
	else:
		req_com = knapSack(peso_max-itens[n-1]['peso'], itens, n-1)
		req_sem = knapSack(peso_max, itens, n-1)
		com_item = itens[n-1]['valor'] + req_com[0]
		sem_item = req_sem[0]

		peso = max(com_item, sem_item)

		if peso == com_item:
			c = [itens[n-1], *req_com[1]]
		else:
			c = [req_sem[1]]

		return [peso, c]



itens = [
	{'id': 1, 'peso': 50, 'valor': 1}, 
	{'id': 2, 'peso': 30, 'valor': 3}, 
	{'id': 3, 'peso': 100, 'valor': 4},
]

peso_max = 150
num = len(itens)
print(knapSack(peso_max, itens, num))
 