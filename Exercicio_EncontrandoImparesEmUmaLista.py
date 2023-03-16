'''Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.
Sua solução deve ser implementada utilizando recursão.
Dica: você vai precisar do método extend() que as listas possuem.'''

def encontra_impares(lista):
    impar = []
    if len(lista) == 0:
        return impar
    elif lista[0] % 2 != 0:
        impar.extend([lista[0]])
    impar.extend(encontra_impares(lista[1:]))
    return impar

lista = [1, 2, 3, 4, 5, 6]
print(encontra_impares(lista))