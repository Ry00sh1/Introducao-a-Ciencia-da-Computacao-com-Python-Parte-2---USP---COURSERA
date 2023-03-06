def menor_nome(nomes):
    menor = nomes[0]
    for nome in nomes:
        if len(nome) < len(menor):
            menor = nome

    return menor

lista_nomes = []
nome = str(input('Digite um nome: '))
nome = nome.strip().capitalize()
lista_nomes.append(nome)

while nome != '':
    nome = str(input('Digite um nome: '))
    nome = nome.strip().capitalize()
    lista_nomes.append(nome)

if '' in lista_nomes:
    lista_nomes.remove('')

print(menor_nome(lista_nomes))