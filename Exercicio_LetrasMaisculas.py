def maiusculas(frase):
    letras_maiusculas = ""
    for letra in frase:
        if letra.isupper():
            letras_maiusculas += letra
    return letras_maiusculas

