def getInfoArchivo (nombre_archivo:str) -> list[str]: 
    archivo = open(nombre_archivo,'r')
    lista_cosas = archivo.readlines()
    lista_retorno = []
    for elemento in lista_cosas:
        lista_retorno.append(elemento.replace('\n',''))
        #print(elemento)
    archivo.close()
    return lista_retorno

def imprimirLista (lista_cosas:list) -> None:
    for i,elemento in enumerate(lista_cosas):
        print(i+1,elemento)

def guardarLista (nombre_archivo:str, lista_cosas:list) -> None:
    archivo = open(nombre_archivo,'w')

    for elemento in lista_cosas:
        archivo.write(str(elemento) + '\n')

    archivo.close()

def stringToDict (string:str, lista_llaves:list[str]) -> dict:
    dict_retorno = {}
    lista_valores = string.split(';')
    for i in range(len(lista_llaves)):
        dict_retorno.update(
            {
                str(lista_llaves[i]) : str(lista_valores[i])
            }
        )
    return dict_retorno