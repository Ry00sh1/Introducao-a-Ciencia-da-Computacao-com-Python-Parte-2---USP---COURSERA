'''Este exercício tem duas partes:
Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. 
Essa função deve ser implementada utilizando recursão.
Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. 
Se n não for maior que 1, a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.
Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").
Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também que é possível transformar números em strings com a função str().
Dica: Será que neste caso a base da recursão é diferente de n==1?
No exemplo de execução abaixo, note que há uma diferença entre como a string é e como ela é interpretada. Na função print o símbolo "\n" é interpretado como quebra de linha'''

def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n < 2:
        return ""
    elif n == 2:
        return "Um elefante incomoda muita gente\n" + str(2) + " elefantes " + incomodam(2) + "muito mais\n"
    else:
        texto = elefantes(n-1)
        texto += str(n-1) + " elefantes incomodam muita gente\n"
        texto += str(n) + " elefantes "+ incomodam(n) + "muito mais\n" 
        return texto

print(elefantes(12))