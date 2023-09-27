import functools
import math

#Exercicio 4.1
impar = lambda x : True if x % 2 != 0 else False

#Exercicio 4.2
positivo = lambda x : True if x >= 0 else False

#Exercicio 4.3
comparar_modulo = lambda x,y : True if abs(x) < abs(y) else False

#Exercicio 4.4
cart2pol = lambda x,y : (math.sqrt(x**2 + y**2), math.atan2(y,x))

#Exercicio 4.5
ex5 = lambda f, g, h : lambda x, y, z : h(f(x,y), g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    return [f(n) for n in lista]
    
#Exercicio 4.8
def subconjunto(lista1, lista2):
    return all(x in lista2 for x in lista1)

#Exercicio 4.9
def menor_ordem(lista, f):
    #if (len(lista) == 1):
    #    return lista[0]
    #
    #if f(lista[0], lista[1]):
    #    lista.pop(1)
    #    return menor_ordem(lista,f)
    #else:
    #    return menor_ordem(lista[1:],f)
   
    return lista[0] if len(lista) == 1 else (menor_ordem(lista[1:], f) if not f(lista[0], lista[1]) else menor_ordem([lista[0]] + lista[2:], f))

    
#Exercicio 4.10
def menor_e_resto_ordem(lista, f):
    return min(lista, key=lambda x: (not f(x, lista[0]), x)), [x for x in lista if x != min(lista, key=lambda x: (not f(x, lista[0]), x))]

    

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    #if len(lista) <= 1:
    #    return lista
    #else:
    #    pivot = lista[0]
    #    less = [x for x in lista[1:] if ordem(x, pivot)]
    #    greater = [x for x in lista[1:] if not ordem(x, pivot)]
    #    return ordenar_seleccao(less, ordem) + [pivot] + ordenar_seleccao(greater, ordem)
    
    return lista if len(lista) <= 1 else ordenar_seleccao([x for x in lista[1:] if ordem(x, lista[0])], ordem) + [lista[0]] + ordenar_seleccao([x for x in lista[1:] if not ordem(x, lista[0])], ordem)
    
