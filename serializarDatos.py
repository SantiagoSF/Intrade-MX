"""
    Cambia los datos del archivo CSV del INEGI por objetos serializados
    en Python para evitar procesar cada vez los miles de lineas del archivo
    CSV. No se incluyen los datos ya serializados puesto que estos deben
    ser serializados en local por el usuario final. Esto por motivos de
    seguridad con el modulo pickle.
    El archivo BCMM.pickle debe estar en la misma carpeta que main.py

Autor: Santiago Sánchez
Github: @SantiagoSF
"""

import csv
import pickle

# Rutas de los archivos CSV
codigo_paises = ''
fracciones_arancelarias = ""
datos_comercio = ""



def p_paises(ruta):
    """ Obtiene los codigos ISO ALPHA 3 de cada pais en el archivo """
    codigo_paises = ruta + "\\data\\paises\\codigo-pais.txt"
    with open(codigo_paises, encoding="utf-8") as codigoPaises:
        # Iniciamos el diccionario de clave: codigo ISO y valor: nombre del pais
        paises = {}
        codigos = csv.reader(codigoPaises, delimiter=',')
        contador = 0
        # codigos_iso = []
        for datos in codigos:
            # Saltamos la primera fila
            if contador == 0:
                contador += 1
            else:
                nombres = dict(zip([datos[0][::]], [datos[1][::]]))
                # Actualizamos el diccionario vacio con este nuevo diccionario
                paises.update(nombres)
                # Ejemplo: print(paises['HKG'] --> 'Hong Kong')
    return paises


def p_fracciones(ruta):
    """ Obtiene las fracciones arancelarias y las relaciona con cada art/categoria
    Liege = Ley de Impuestos Generales de Importacion y Exportacion """
    fracciones_arancelarias = ruta + "\\data\\ligie\\tc_tigie.csv"

    with open(fracciones_arancelarias, encoding="utf-8") as Ligie:
        fracciones = csv.reader(Ligie, delimiter=',')
        codigos_mercancias = {}
        contador = 0
        for datos in fracciones:
            if contador == 0:
                contador += 1
            else:
                fraccion = dict(zip([datos[0][::]], [datos[1][::]]))
                codigos_mercancias.update(fraccion)
    return codigos_mercancias


def p_balanza(ruta):
    """ Devuelve una lista de listas Obtiene los datos 
    con formato: [año, tipo, pais_o_d, fraccion, cantidad(MXN)] """
    datos_comercio = ruta + "\\data\\comercio\\bcmm_anual_tr_cifra_2018.csv"

    with open(datos_comercio, encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        contador = 0
        balanza_comercial = []
        for row in csv_data:
            if contador == 0:
                contador += 1
            else:
                if contador == 1:  # Saltamos la segunda linea(TOTAL) de la balanza
                    contador += 1
                else:
                    if row[9] != '' and row[7] != '':
                        balanza_comercial.append(
                                                [row[2], row[3], row[7],
                                                    row[5], row[9]]
                                                )
    return balanza_comercial


# Serializa los datos para no volver a realizar el proceso de lectura
def go_serialize(ruta):
    """Esta funcion serializa los datos de los tres archivos csv necesarios
    para que el programa funcione: 1.-ISO3.csv 2.-ligie.csv 3.-BCMM"""
    
    paises = p_paises(ruta)
    codigos_mercancias = p_fracciones(ruta)
    balanza_comercial = p_balanza(ruta)

    datos = {
        'paises': paises,
        'codigos mercancias': codigos_mercancias,
        'balanza': balanza_comercial
        }
    
    ruta = ruta + "\\serialized\\BCMM.pickle"
    with open(ruta, 'wb') as file:
        pickle.dump(datos, file)
