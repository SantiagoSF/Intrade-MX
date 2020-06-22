"""
Grafica los datos de la balanza comercial con matplotlib
Lo realiza por tipo de operacion y pidiendo el codigo arancelario
de la mercancia por tkinter

Autor: Santiago Sánchez
Github: @SantiagoSF
"""

import pickle
from matplotlib import pyplot as plt


with open('BCMM.pickle', 'rb') as pickle_file:
    datos = pickle.load(pickle_file)

paises_por_codigo = datos['paises']
mercancias = datos['codigos mercancias']
balanza_comercial = datos['balanza']

# Plot bottom and top margins
bottom = 0.25  # the bottom of the subplots of the figure
top = 0.94     # the top of the subplots of the figure


def consulta(fraccion, tipo):
    """ Grafica los datos solicitados en una nueva ventana """

    plt.close('all')  # Cierra todas las graficas si es que existen
    x = []
    y = []
    # Coleccion = Coleccion de datos en balanza_comercial
    # [0)tipo, 1)año, 2))pais_o_d, 3)fraccion, 4)cantidad(MXN)]
    for coleccion in balanza_comercial:
        if coleccion[3] == fraccion and coleccion[0] == tipo:
            x.append(paises_por_codigo.get(coleccion[2]))
            y.append(int(coleccion[4]))
            plt.bar(
                paises_por_codigo.get(coleccion[2]) + '\n' + "{:,}".format(int(coleccion[4])),
                int(coleccion[4]),
                label=paises_por_codigo.get(coleccion[2]) +
                " {:,}$".format(int(coleccion[4])),
                width=0.8
                )
    try:
        plt.title("{0} de '{1:.100}...' por paises compradores".format(
            tipo, mercancias.get(fraccion)))
    except:
        print('No se encontro los datos solicitados')
    
    plt.yscale('log')
    plt.legend()
    plt.xlabel('Paises y cantidades en Moneda Nacional')
    plt.xticks(rotation=45)
    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)
    plt.grid(True)
    plt.subplots_adjust(bottom=bottom, top=top)
    plt.show()