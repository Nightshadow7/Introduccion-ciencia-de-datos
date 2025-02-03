# Introduccion a Ciencia de Datos 

Anexo una Breve descripcion de los datos encontrados en Este Repositorio

## Modulos de Aprendizaje
| Modulo | Descripcion | Ejercicios | 
| -- | -- | -- |
| Basicos | En este modulo se explican cada una de las variables y los operadores arirmeticos. |[Ejemplos Basicos](Ejemplos%20basicos.py#L1) |
| Control o Flujo | En este modulo se explican cada una de las estructuras de control. | [Ejemplos de Control y Flujo](Ejemplos%20control%20flujo.py#L1) |
| Funciones o Clases |  Declaración de funciones, argumentos, y funciones anónimas y Introducción a POO (Programación Orientada a Objetos). | [Funciones y Clases](Ejemplos%20funciones%20clases.py#L1) |
| Estructuras de datos | En este modulo se explican operaciones con listas, diccionarios, claves, valores, tuplas y conjuntos. |
| Avanzado |  En este modulo explicaremos decoradores, Introducción a async/await y leer y escribir archivos. |

## Definiciones de Modulos
### [Basicos](Ejemplos%20basicos.py#L1)
1. **[Variables y Tipos de Datos](Ejemplos%20basicos.py#L3)**
    + __Variable__: Es un contenedor que almacena datos. Se declara asignándole un valor con el operador **=**.
    + __Tipos de datos principales en Python__:
      + __int__: Números enteros, como ___5___ o ___-10___.
      + __float__: Números decimales, como 3.14 o -0.5.
      + __str__: Cadenas de texto, como ___"Hola"___ o ___'Python'___.
      + __bool__: Valores lógicos, ___True___ o ___False___.
      + __list__: Listas, una colección ordenada y mutable de elementos.
      + __tuple__: Tuplas, una colección ordenada pero inmutable.
      + __dict__: Diccionarios, una colección de pares ___clave-valor___.
      + __set__: Conjuntos, una colección no ordenada de elementos únicos.
2. **[Operadores](Ejemplos%20basicos.py#L39)**
    + __Operadores aritméticos__: Realizan operaciones matemáticas.
      + **Suma**: +
      + **Resta**: -
      + **Multiplicacion**: *
      + **División**: /
      + **División entera**: // 
      + **Módulo**: % 
      + **Potencia**: ** 

    + __Operadores de comparación__: Comparan dos valores y devuelven ___True___ o ___False___.
      + **Igual a**: ==
      + **Distinto de**: !=
      + **Menor que**: <
      + **Mayor que**: >
      + **Menor o igual a**: <=
      + **Mayor o igual a**: >=
    + __Operadores lógicos__: Operaciones sobre valores ___booleanos___.
      + **and**: Verdadero si ambos operandos son ___True___.
      + **or**: Verdadero si al menos uno de los operandos es ___True___.
      + **not**: Invierte el valor lógico.
    + __Operadores de asignación__: Asignan valores a variables. 
      + **Igual**: =
      + **Operaciones con asignación**: +=, -=, *=, /=, etc.

### [Control o flujo](Ejemplos%20control%20flujo.py#L1)
**Estructuras de control en Python**: Las estructuras de control permiten ejecutar código de forma condicional o repetitiva. Aquí están las principales:
1. **[Condicionales](Ejemplos%20control%20flujo.py#L4) (if, elif, else)**
    Permiten ejecutar bloques de código basados en condiciones.
    ```python
    if condicion:
      # Código si la condición es verdadera
    elif otra_condicion:
      # Código si otra condición es verdadera
    else:
      # Código si ninguna condición es verdadera
    ```
2. **[Bucles](Ejemplos%20control%20flujo.py#L14) (while, for)**
  Ejecutan bloques de código repetidamente mientras se cumple una condición o iteran sobre elementos de una colección.
    + **while**: Repite un bloque mientras una condición es verdadera.
    + **for**: Itera sobre los elementos de una secuencia (lista, rango, etc.).
    ```python
    for elemento in secuencia:
      # Código a ejecutar
    ```
3. **[Manejo de excepciones](Ejemplos%20control%20flujo.py#L32) (try, except)**
  Gestionan errores en tiempo de ejecución de manera controlada.
    ```python
    try:
      # Código que puede generar un error
    except TipoDeError:
      # Código a ejecutar si ocurre el error
    ```
4. **[match-case](Ejemplos%20control%20flujo.py#L39) (Introducido en Python 3.10)**
  Similar al switch en otros lenguajes, permite evaluar patrones específicos.
    ```python
    match variable:
      case valor1:
        # Código para el caso valor1
      case valor2:
        # Código para el caso valor2
      case _:
        # Código por defecto
    ```

### [Funciones y Clases](Ejemplos%20funciones%20clases.py#L1)
1. **[Funciones](Ejemplos%20funciones%20clases.py#L4)**
Las funciones son bloques de código reutilizables que realizan tareas específicas. 
    + **Definicion**:
      ```python
      def nombre_funcion(parametros):
        # Cuerpo de la función
        return valor
      ```
    + **Componentes**:
      + **def**: Palabra clave para definir una función.
      + **nombre_funcion**: Identificador único de la función.
      + **parametros**: Valores que recibe la función como entrada.
      + **return**: Devuelve un valor (opcional).
2. **[Clases](Ejemplos%20funciones%20clases.py#L29)**
Las clases son plantillas para crear objetos, que son instancias de datos estructurados que pueden incluir propiedades (atributos) y comportamientos (métodos).
    + Definición:
      ```python
      class NombreClase:
        def __init__(self, parametros):
          # Constructor para inicializar atributos
        def metodo(self):
          # Método de la clase
      ```

### [Estructuras de Datos](Ejemplos%20estructuras%20datos.py#L1)
1. **[Manejo de Archivos en Python](Ejemplos%20estructuras%20datos.py#L4)**
Python permite trabajar con archivos para leer, escribir, y manipular datos. Esto es esencial para tareas como el análisis de datos, el registro de **logs**, o la interacción con bases de datos de texto.
  **Operaciones principales con archivos:**
    + **Apertura de archivos** (**open**):
      + **Modo de apertura**:
        + **Lectura** (predeterminado): 'r'
        + **Escritura** (sobrescribe el archivo): 'w'
        + **Escritura** (agrega al final del archivo): 'a'
        + **Lectura y escritura**: 'r+'
        + **Sintaxis**
          ```python
          archivo = open("nombre_archivo.txt", modo)
          ```
      + **Lectura de archivos**:
        + **Leer todo el contenido**: *archivo.read()*.
        + **Leer línea por línea**: *archivo.readline()*.
        + **Leer todas las líneas como una lista**: *archivo.readlines()*.
      + **Escritura en archivos**:
        + **Escribir texto**: *archivo.write*("Texto a escribir\n").
      + **Cierre de archivos**: 
        + **archivo.close()** cierra el archivo para liberar recursos.
        + Con la declaración **with**, no es necesario cerrarlo manualmente
          ```python
          with open("archivo.txt", "r") as archivo:
            contenido = archivo.read()
          ```
2. **[Estructuras de datos](Ejemplos%20estructuras%20datos.py#L45)**
Además de las estructuras de datos básicas como listas, tuplas, diccionarios y conjuntos, Python ofrece herramientas y librerías para trabajar con estructuras avanzadas. Algunas de ellas son:
    + **Listas anidadas**:
      + Son listas dentro de listas, útiles para trabajar con datos tabulares.
      + Ejemplo: \[[1, 2], [3, 4]]
    + **Pilas y Colas**:
      + **Pilas (Stack)**: Usan el principio ___LIFO___ (Last In, First Out).
      + **Colas (Queue)**: Usan el principio ___FIFO___ (First In, First Out).
      + Se pueden implementar con listas o con la librería ___collections___.
    + **Diccionarios anidados:**
      + Permiten crear estructuras jerárquicas, como registros complejos.
      + Ejemplo:
        ```python
        {"usuario1": {"nombre": "Juan", "edad": 25}}
        ```
    + **Conjuntos avanzados:**
      Operaciones como unión, intersección y diferencia entre conjuntos.
    + **Uso de *collections*:**
      + **deque**: Estructura eficiente para colas.
      + **defaultdict**: Diccionario con valores predeterminados.
      + **Counter**: Conteo de elementos en colecciones.





## Ejemplos de  clase
| Tema | Descripcion | Practica |
| -- | -- | -- |
| Introduccion a Python | Iniciacion con el Hola mundo | [Hello World](Ejemplo%20clase%201.py#L3) |
| Variables y Tipos de Datos | Introducimos los principales tipos de datos en Python y el casting | <ul><li>[Tipos de datos](Ejemplo%20clase%202_1.py#L1)</li> <li>[Ejemplo de uso](Ejemplo%20clase%202_2.py#L1)</li></ul> |
| Estructuras de control | Se muestran un pequeño vistaso al uso de las estructuras de control y las funciones | [Estructuras de Control](Ejemplo%20clase%203.py#L1) |
| Estructura de datos | Se muestran los tipos de estructuras de datos basicos como arrays y matrices tambien el como manipularlos. | [Arrays y Matrices](Ejemplo%10clase%204.py#L1) |
| Juego pokemon | Se muestra la estructura de un juego de pokemones creado y proporcionado por el docente | [Juego Pokemon version 0.0](pokemonGame.py#L132)


## Ejercicios
| # | Descripcion del Ejercicio | Ejercicio |
| -- | -- | -- |
| Sistema de Facturacion Simple | Crear un programa que le permita al usuario generar una factura básica con múltiples productos.  | [Facturacion simple](Facturacion%20simple.py#L83) |
| Analisis de Palabras | Escribe un programa que analice un texto introducido por el usuario. | [Introduccion del texto](Texto%20introducido.py#L50) |
| Rotacion de matriz | Dada una matriz cuadrada, escribe un programa que realice la rotación de 90 grados en sentido horario y muestre la matriz rotada. | <ul><li>[Rotacion con numpy](Rotacion%20matriz.py#L32)</li><li>[Rotacion sin Librerias](Rotacion%20matriz.py#L72)</li></ul> |
| Modificacion del juego de Pokemon | Se investigo al respecto en la pagina oficial llamada Bulbapedia. Se utilizo un archivo JSON para cargar los movimientos y ataques,adicional como recomendacion cabiar la ruta de archivo para que funcione correctamente. [Aqui👆🏻](Pokemon%20Game%20Released.py#L122) | <ul><li>[Pagina Oficial](https://bulbapedia.bulbagarden.net/wiki/Main_Page)</li><li>[JSON Utilizado](https://github.com/Purukitto/pokemon-data.json)</li><li>[Juego](Pokemon%20Game%20Released.py#L170)</li><ul/> |
