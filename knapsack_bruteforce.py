def knapSack(peso_max, itens, n):
	if n == 0:
		return 0

	if (itens[n-1]['peso'] > peso_max):
		return knapSack(peso_max, itens, n-1)
 
	else:
		return max(
            itens[n-1]['valor'] + 
			knapSack(peso_max-itens[n-1]['peso'], itens, n-1), 
			knapSack(peso_max, itens, n-1))

itens = [
	{'peso': 12, 'valor': 60}, 
	{'peso': 30, 'valor': 300}, 
	{'peso': 20, 'valor': 120},
	{'peso': 25, 'valor': 235}, 
	{'peso': 100, 'valor': 20}
]

peso_max = 150
num = len(itens)
print(knapSack(peso_max, itens, num))
 