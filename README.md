# Cajero Automatico
## Jurgen Sanclemente
El cajero posee las funcionalidades de leer archivos y por consola ( la parte de consola aún sigue en pruebas )

## ¿Como utilizar?

Al iniciar debe seleccionar (2) para leer los 3 archivos de texto, se despliega una lista de acciones paso a paso que va realizando el programa y al final de cada archivo mostrara los datos ( consignaciones totales, retiros total y el dinero actual ).

# Explicacion codigo
Existen 3 carpetas principales y el archivo main.py.

main: Funciona para seleccionar si se utilizaran datos de la consola o los archivos
Impresiones: Posee archivos que realizan impresiones generales a lo largo de la aplicacion
leer_archivo: Para leer linea por linea los diferentes archivos y convertirlos en las peticiones que utiliza la capa logica del sistema
procesar_peticiones: Recibe las tuplas de leer_archivo o en su defecto, los datos por consola, se realizan los calculos y utiliza servicios como el de impresiones para modelar.


La mayoria de partes de la aplicacion son clases ( POO ) pero hay funciones en impresiones que son normales, ya que se utilizan a lo largo de la app y no hay necesidad de instancias.



