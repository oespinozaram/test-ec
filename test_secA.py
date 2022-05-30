import secA


def test_contar():
    cad = "hola mundo"
    assert secA.contar_vocales(cad) == 4

def test_reemplaza():
    cad = "hola mundo"
    assert secA.reemplaza_vocales(cad) == "hule mandu"
