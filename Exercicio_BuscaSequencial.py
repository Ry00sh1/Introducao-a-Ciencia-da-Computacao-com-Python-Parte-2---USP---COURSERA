"""Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca sequencial.
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False."""

def busca(lista, elemento):
    '''O método abaixo é mais fácil e menor, porém na correção não permitiram o uso do método .index()
    if elemento in lista:
        return  lista.index(elemento)
    return False'''
    for item in range(len(lista)):
        if lista[item] == elemento:
            return item
        return False