import funciones

texto_archivo = funciones.getInfoArchivo('animales.csv')
lista_animales = []
lista_llaves = ['nombre','tipo','color']

for linea in texto_archivo:
    lista_animales.append(
        funciones.stringToDict(linea, lista_llaves)
    )

funciones.imprimirLista(lista_animales)