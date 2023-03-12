'''Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. 
Utilize o algoritmo bubble sort.
Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista toda vez que fizer uma alteração em seus elementos.'''

def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        troca = False
        for j in range(0, tamanho-i-1):
            if lista[j] > lista[j+1]:
                lista[j+1], lista[j] = lista[j], lista[j+1] # inverte a posição dos elementos
                print(lista)
                troca = True
                if troca == False: #se não houve nenhuma troca significa que a lista já está ordenada
                    break  #cancela o comando 'for'
    return lista
