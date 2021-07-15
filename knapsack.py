from random import randint
recursoes = 0
tabelado = 0

def knapSack(peso_restante, itens, n, table, itens_na_mochila=[]):
	global recursoes
	global tabelado
	recursoes += 1

	# Fim da mochila
	if n == 0:
		return [0, itens_na_mochila]

	# Verifica se item cabe na mochila
	elif itens[n-1]['peso'] > peso_restante:
		return knapSack(peso_restante, itens, n-1, table, itens_na_mochila)
	
	# Verifica se ja foi calculado
	elif table[n-1][peso_restante] != 'NOT_DEFINED':
		tabelado += 1
		return table[n-1][peso_restante]

	# Testa possibilidades
	else:
		recComItem = knapSack(peso_restante-itens[n-1]['peso'], itens, n-1, table)
		reqSemItem = knapSack(peso_restante, itens, n-1, table)
		valorComItem = itens[n-1]['valor'] + recComItem[0]
		valorSemItem = reqSemItem[0]

		# Verifica a mochila com o maior valor
		if valorComItem > valorSemItem: 	
			valorDaMochila = valorComItem
			c = [itens[n-1], *recComItem[1]]
		else:
			valorDaMochila = valorSemItem
			c = [*reqSemItem[1]]

		# Coloca calculo na tabela
		table[n-1][peso_restante] = [valorDaMochila, c]

		return [valorDaMochila, c]

tamanhos = [20]

listaDeItens = []
for tam in tamanhos:
	itens = []
	for i in range(tam):
		itens.append({'id': i, 'peso': randint(150, 500), 'valor': randint(300, 1000)})
	listaDeItens.append(itens) 

pesos = [1500, 2000]

for itens in listaDeItens:
	for i in pesos:
		print(f'Para {len(itens)} itens, (programação dinamica)')
		print('Itens: ')
		for j in itens:
			print(j)
		print()
		recursoes = 0
		tabelado = 0

		peso_max = i

		num = len(itens)

		table = []
		for _ in range(len(itens)+1): # Tabela NxW (Quantidade de itens por Peso max)
			aux = []
			for _ in range(peso_max+1):
				aux.append('NOT_DEFINED')
			table.append(aux)

		pesoFinal = 0
		mochila = knapSack(peso_max, itens, num, table)

		print(f'Peso {peso_max}: Recursões =', recursoes, 'Buscas na tabela =', tabelado)
		print('Valor da mochila:', mochila[0])
		for it in mochila[1]:
			print(it)
			pesoFinal += it['peso']
		print('Peso final da mochila:', pesoFinal)
		print()
		print()