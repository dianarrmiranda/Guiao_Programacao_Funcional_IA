#Exercicio 1.1
def comprimento(lista):
	if not lista:
		return 0
	else:
		return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if not lista:
		return 0
	else:
		return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if not lista :
		return False
	elif lista[0] == elem:
		return True
	return existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if not l2:
		return l1
	else:
		l1.append(l2[0])

	return concat(l1, l2[1:])

#Exercicio 1.5
def inverte(lista):
	if not lista:
		return []
	else:
		return [lista[-1]] + inverte(lista[:-1])

#Exercicio 1.6
def capicua(lista):
	if len(lista) <= 1:
		return True
	elif lista[0] == lista[-1]:
		return capicua(lista[1:-1])
	else:
		return False

#Exercicio 1.7
def concat_listas(lista):
	if not lista:
		return []
	else:
		return lista[0] + concat_listas(lista[1:])

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista:
		return []
	else:
		if lista[0] == original:
			lista[0] = novo
		return [lista[0]] + substitui(lista[1:], original, novo)
	

#Exercicio 1.9
def fusao_ordenada(lista1, lista2):
	if not lista1:
		return lista2
	if not lista2:
		return lista1
	
	if lista1[0] > lista2[0]:
		return [lista2[0]] + fusao_ordenada(lista1, lista2[1:])
	elif lista1[0] < lista2[0]:
		return [lista1[0]] + fusao_ordenada(lista1[1:], lista2)
	else:
		return [lista1[0], lista2[0]] + fusao_ordenada(lista1[1:], lista2[1:])

#Exercicio 1.10
def lista_subconjuntos(lista):
	if len(lista) == 0:
		return [[]]
	else:
		subElements = lista_subconjuntos(lista[1:])
		return subElements + [[lista[0]] + subElement for subElement in subElements]
	

#Exercicio 2.1
def separar(lista):
    if len(lista) == 0:
        return ([], [])
    
    subFirst, subSecond = separar(lista[1:])
    
    return ([lista[0][0]] + subFirst, [lista[0][1]] + subSecond)

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if not lista:
		return ([], 0)
	
	subFirst, subSecond = remove_e_conta(lista[1:], elem)

	if elem == lista[0]:
		return (subFirst, 1 + subSecond)
	else:
		return ([lista[0]] + subFirst, subSecond)
	
#Exercicio 2.3
def num_ocorrencias(lista):
	if not lista:
		return []
	firstElement = lista[0]
	ocorrencias = lista.count(firstElement)
	
	rest = []
	for element in lista:
		if element != firstElement:
			rest.append(element)
	
	return [(firstElement, ocorrencias)] + num_ocorrencias(rest)


#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    pass

#Exercicio 3.4
def menor(lista):
	pass

#Exercicio 3.6
def max_min(lista):
	pass
