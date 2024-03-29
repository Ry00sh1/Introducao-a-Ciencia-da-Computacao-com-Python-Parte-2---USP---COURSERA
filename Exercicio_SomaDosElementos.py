'''Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.
Sua solução deve ser implementada utilizando recursão.'''
def soma_lista(lista):
    if len(lista) == 0:
        return 'lista vazia'
    elif len(lista) == 1:
        return lista[0]
    else: 
        n = len(lista)
        primeiro = lista[0]
        return primeiro + soma_lista(lista[1:n])