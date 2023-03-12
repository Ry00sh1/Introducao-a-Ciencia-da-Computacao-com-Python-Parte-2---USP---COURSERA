"""Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e 
devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada."""

def ordenada(lista):
    if len(lista) <= 1: 
        return True
    crescente = all(lista[item] <= lista[item+1] for item in range(len(lista)-1))
    
    decrescente = all(lista[item] >= lista[item+1] for item in range(len(lista)-1))

    #função 'all' retorna True se todos os elementos da lista comprirem os requisitos, caso contrário, False

    return crescente or decrescente #caso cescente ou decrescente forem verdadeiros, retorna True, caso contrário, False
