# Intrade-MX
Programa en Python para consultar los datos abiertos de la balanza comercial de mercancías de México de manera gráfica


### Caracteristicas

- Consulta los datos abiertos del INEGI por fraccion arancelaria y operacion comercial (Exportacion/Importacion)
- Los grafica usando matplotlib. Las graficas contienen los paises que realizan la operacion y el monto en pesos mexicanos


## Este programa utiliza
1. Python 3
2. tkinter
3. matplotlib
4. csv
5. pickle

------------



### Nota
Este programa pasa los datos del archivo CSV a listas y diccionarios Python. Estos se serializan para ser usador por el programa para evitar leer el archivo csv completo cada consulta.
**Los archivos .pickle no son incluidos. Estos deben ser serializados en local para evitar riesgos de seguridad. Solo se incluyen los archivos CSV del INEGI. (https://docs.python.org/3/library/pickle.html)**
