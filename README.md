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
### Como hacer consultar de mercancías
El programa realiza las gráficas por mercancía y por tipo de operación: Exportación/Importación.
Para consultar una determinada mercancía se ingresa su fracción arancelaria. Por ejemplo: **09012101**  es la fracción arancelaria del café sin descafeinar. Exportación y te graficara los países a los que exportamos dicha fracción arancelaria.
Las fracciones arancelarias se fundamentan el en Sistema armonizado elaborado por la Organización Mundial de Aduanas (OMA. Es un sistema de clasificación de mercancías multipropósito para catalogar los productos. Este se usa en el comercio internacional. Tiene como objetivos:
1. Facilitar el intercambio comercial y de información.
2. Armonizar la descripción, clasificación y codificación de mercancías.
3. Ayudar a definir aranceles aduaneros.
4. Recopilar estadísticas de comercio exterior.
5. Establecer impuestos internos, políticas comerciales, reglas de origen, tarifas de flete, precios, etc.

**México** sustenta su comercio exterior en las normas y lineamientos de la OMC y la OMA. No obstante como otros países, México añade ciertos elementos.  En México, la Ley de los Impuestos Generales de Importación y Exportación (LIGIE) toma en cuenta la clasificación arancelaria. Cada producto se identifica con ocho dígitos o números específicos:
1. Los dos primeros números son para reconocer el capítulo al que pertenecen las mercancías dentro del Sistema Armonizado de Designación y Codificación de Mercancías.
2. Los números tres y cuatro son para la partida arancelaria. Por ejemplo, las  plantas tienen una partida diferente a la que tienen los objetos de arte.
3. Los dígitos cinco y seis son para conocer la subpartida arancelaria.
4. Los últimos dos dígitos (siete y ocho) se aplican de forma local en México.
**09012101** del café es 09 para el capitulo, 01 para la partida 21 para la subpartida y 01 constituye la fracción. **09012101** es la clasificación arancelaria del café sin descafeinar.

![alt text](https://iili.io/JLbjXn.png)


Puede encontrar todo el desglose de todas las mercancías en México aquí 
--> http://www.siicex-caaarem.org.mx/
También puede realizar consulta de clasificación arancelaria para una determinada mercancía en la Ventanilla Única de Comercio Exterior (VUCEM) aquí 
--> https://www.ventanillaunica.gob.mx/vucem/Clasificador.html


## Git workfow
Este repositorio usa git LFS (git Large File Storage) para manejar los archivos CSV del INEGI los cuales son: 
	a) Balanza comercial de mercancias de México
	b) Tarifa de la Ley de los Impuestos Generales de Importación y Exportación (TIGIE)

https://help.github.com/es/github/managing-large-files/collaboration-with-git-large-file-storage

Para poder trabajar con este repositorio de la forma estandar es necesario instalar git LFS
https://git-lfs.github.com/
Si no cuentas con git lfs y clonas el repositorio no descargaras los archivos csv necesrio para el programa. Solo descargaras los punteros a los archivos.

### Nota
Este programa pasa los datos del archivo CSV a listas y diccionarios Python. Estos se serializan para ser usador por el programa para evitar leer el archivo csv completo cada consulta.
**Los archivos .pickle no son incluidos. Estos deben ser serializados en local para evitar riesgos de seguridad. Solo se incluyen los archivos CSV del INEGI. (https://docs.python.org/3/library/pickle.html)**