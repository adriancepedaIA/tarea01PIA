# Problema 1. Procesamiento de una lista de enteros
def procesar_lista_enteros(lista):
    lista_procesada = []

    for numero in lista:
        if numero >= 0 and numero not in lista_procesada:
            lista_procesada.append(numero)

    lista_procesada.sort()

    return lista_procesada

# Problema 2. Frecuencia de palabras en un texto
def frecuencia_palabras(lista_palabras, ruta_texto):
    import string

    # Aunque no lo diga el enunciado, convierto el listado a minúsculas para que pueda encontrar las palabras
    frecuencia = {palabra.lower(): 0 for palabra in lista_palabras}

    with open(ruta_texto, 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower()
        texto = texto.translate(str.maketrans('', '', string.punctuation))
        palabras_texto = texto.split()

        for palabra in palabras_texto:
            if palabra in frecuencia:
                frecuencia[palabra] += 1

    frecuencia_ordenada = dict(sorted(frecuencia.items()))

    return frecuencia_ordenada

# Problema 3. Trabajo con conjuntos
def trabajo_conjuntos(conjunto_a, conjunto_b):
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)

    resultado = {
        'interseccion': set_a.intersection(set_b),
        'union': set_a.union(set_b),
        'diferencia_simetrica': set_a.symmetric_difference(set_b)
    }

    return resultado

# Pruebas de funcionamiento
if __name__ == "__main__":
    # Prueba del Problema 1
    lista_ejemplo = [4, -1, 2, 4, 3, -5, 2]
    resultado = procesar_lista_enteros(lista_ejemplo)
    print("Problema 1.Lista procesada:", resultado)

    # Prueba del Problema 2
    lista_palabras = ["caballero", "rocín", "señora", "hidalgo", "Sancho", "Dulcinea"]
    ruta_texto = "apartado_2_problema_2_texto.txt"
    resultado_frecuencia = frecuencia_palabras(lista_palabras, ruta_texto)
    print("Problema 2.Frecuencia de palabras:", resultado_frecuencia)

    # Prueba del Problema 3
    conjunto_a = [1, 2, 3, 4, 5]
    conjunto_b = [4, 5, 6, 7, 8]
    resultado_conjuntos = trabajo_conjuntos(conjunto_a, conjunto_b)
    print("Problema 3.Trabajo con conjuntos:", resultado_conjuntos)