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
	if(not lista):
		return None
	else:
		return lista[0]
	
#Exercicio 3.2
def cauda(lista):
	if(not lista):
		return None
	else:
		return lista[1:]
	
#Exercicio 3.3
def juntar(l1, l2):
	if(len(l1) != len(l2)):
		return None
	
	if(not l1 and not l2):
		return []
	
	return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])
		 

#Exercicio 3.4
def menor(lista):
	if(not lista):
		return None
	
	if(len(lista) == 1):
		return lista[0]
	
	rest = menor(lista[1:])
	if(lista[0] > rest):
		return rest
	else:
		return lista[0]
	
#Exercicio 3.5
def menor_resto(lista):
	if(not lista):
		return None
	
	if(len(lista) == 1):
		return lista[0], []
	
	menor = min(lista)
	listaSemMenor = []

	for x in lista:
		if x != menor:
			listaSemMenor.append(x)
	
	menorRest, rest = menor_resto(listaSemMenor)

	return menor, [menorRest] + rest
	
#Exercicio 3.6
def max_min(lista):
	if(not lista):
		return None
	
	if(len(lista) == 1):
		return (lista[0], lista[0])
	
	rest = max_min(lista[1:])

	if(lista[0] > rest[0]):
		return (lista[0], rest[1])
	elif(lista[0] < rest[1]):
		return (rest[0], lista[0])
	else: 
		return (rest[0], rest[1])
	
#Exercicio 3.7
def menor2_rest(lista):
	if(not lista):
		return None
	if len(lista) == 1:
		return lista[0], None, []  # Retorna o único elemento como o menor e None para o segundo menor, com uma lista vazia
	
	menor1 = min(lista)
	listaSemMenor1 = [x for x in lista if x != menor1]
	
	menor2 = min(listaSemMenor1)
	listaSemMenor2 = [x for x in listaSemMenor1 if x != menor2]
	
	menor1rest, menor2rest, rest = menor2_rest(listaSemMenor2)
	
	if menor2rest is None:
		return menor1, menor2, [menor1rest] + rest
	else:
		return menor1, menor2, [menor1rest, menor2rest] + rest

#Exercicio 3.8
def media_mediana(lista):
	if not lista:
		return None
	
	if len(lista) == 1:
		return (lista[0], lista[0])
	
	media_resto = media_mediana(lista[1:])

	if(len(lista)%2 == 0):
		return ((lista[0] + len(lista[1:]) * media_resto[0]) / len(lista), (lista[int(len(lista)/2)-1] + lista[int(len(lista)/2)])/2)
	else:
		return ((lista[0] + len(lista[1:]) * media_resto[0]) / len(lista), lista[int(len(lista)/2)] )
	
#Teste Ex 2.3
print("Exercicio 2.3: ")
lista = [5, 3, 9, 1, 7, 5, 5, 3, 3, 3, 3, 9]
print(num_ocorrencias(lista))
print()

#Teste Ex 3.1
print("Exercicio 3.1: ")
lista = [5, 3, 9, 1, 7]
print(cabeca(lista))
lista = []
print(cabeca(lista))
print()

#Teste Ex 3.2
print("Exercicio 3.2: ")
lista = [5, 3, 9, 1, 7]
print(cauda(lista))
lista = []
print(cauda(lista))
print()

#Teste Ex 3.5
print("Exercicio 3.5: ")
lista = [5, 3, 9, 1, 7]
print(menor_resto(lista))
lista = []
print(menor_resto(lista))
print()

#Teste Ex 3.6
print("Exercicio 3.6: ")
lista = [5, 3, 9, 1, 7]
print(max_min(lista))
lista = []
print(max_min(lista))
print()

#Teste Ex 3.7
print("Exercicio 3.7: ")
lista = [5, 3, 9, 1, 7]
print(menor2_rest(lista))
lista = []
print(menor2_rest(lista))
print()

#Teste Ex 3.8
print("Exercicio 3.8: ")
lista = [1, 2, 3, 4, 7, 19, 20]
print(media_mediana(lista))
lista = [1, 2, 3, 4, 5, 6]
print(media_mediana(lista))
lista = []
print(media_mediana(lista))
print()