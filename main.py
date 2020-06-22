""" 
    Aplicacion gráfica para observar los datos abiertos del INEGI
    sobre la Balanza Comercial de Mercancias Mexicana (BCMM) al año.
    El programa se divide en dos ventanas:
        1.-La primera sirve para introducir la mercancia por tipo
        de fraccion arancelaria y por tipo de operacion.
        2.-La segunda es una ventana de matplotlib con la grafica.
        Todo lo necesario para esto esta en el modulo 'graficar'

Autor: Santiago Sánchez
Github: @SantiagoSF

 """

import tkinter as tk
import os
import graficar
from serializarDatos import go_serialize


def graph():
    """ Llama a la funcion consulta del modulo graficar para obtener
        la ventana de matplotlib """
    fraccion = txt.get()
    opcion = operacion.get()
    # Transforma los valores del boton tkinter a strings
    if opcion == 1:
        opcion = 'Exportaciones'
    else:
        opcion = 'Importaciones'

    graficar.consulta(fraccion, opcion)


def serialize():
    """Crea los modulos pickle para los datos obtenidos del archivo csv"""

    if os.name == 'nt':
        ruta = os.path.join(os.getcwd() + "\\serialized")
        archivo = '\\BCMM.pickle'
    else:
        ruta = os.path.join(os.getcwd() + "/serialized")
        archivo = '/BCMM.pickle'

    # Si el archivo BCMM.pickle existe: continuar
    if os.path.isfile(ruta + archivo) == True:
        pass

    # De no existir se crea
    else:
        go_serialize(os.getcwd())

serialize()

# iniciamos la ventana con el titulo y obtenemos el valor del cuadro de texto
window = tk.Tk()
window.wm_title("Intrade MX")
operacion = tk.IntVar()


# Empaquetamos los widgets para ingresar la fraccion arancelaria
lbl = tk.Label(window, text="Fraccion Arancelaria: ")
lbl.pack()
txt = tk.Entry(window, width=40)
txt.pack()

# Empaquetamos los tipos de operacion disponibles
op1 = tk.Radiobutton(window, text='Exportaciones', value=1, variable=operacion)
op2 = tk.Radiobutton(window, text='Importaciones', value=2, variable=operacion)
op1.pack()
op2.pack()

# Boton que llama a la funcion clicked (consulta)
btn = tk.Button(window, text="Graficar!", command=graph)
btn.pack()


def _quit():
    """ Detiene mainloop. Esto es necesario en windows para prevenir
        un Fatal Python Error: PyEval_RestoreThread: NULL tstate"""
    window.quit()
    window.destroy()


button = tk.Button(master=window, text="Salir", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()
# Si se pone windows.destroy() aqui causara un error si la ventana
# se cierra con el gestor de ventanas
