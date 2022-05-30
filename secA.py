# conteo de vocales y reemplazo de siguiente vocal


def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c in "aeiou":
            voc = voc + 1
    return voc


def reemplaza_vocales(cad):
    # siguiente vocal
    n_cad = ""
    for c in cad:
        if c == "a":
            n_cad = n_cad + "e"
        elif c == "e":
            n_cad = n_cad + "i"
        elif c == "i":
            n_cad = n_cad + "o"
        elif c == "o":
            n_cad = n_cad + "u"
        elif c == "u":
            n_cad = n_cad + "a"
        else:
            n_cad = n_cad + c
    return n_cad


if __name__ == '__main__':
    cad = "hola mundo"
    print(contar_vocales(cad))
    print(reemplaza_vocales(cad))
