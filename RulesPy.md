# Guia para hacer contribuciones al repositorio #

## Resumen

Este es un resumen

## Tabla de contenido

1. [Variables](#variables)
2. [Funciones(#funciones)]
3. [Clases](#clases)
4. [Separacion de bloques de codigo](#organizacion)
5. [Archivos y organizacion](#manejodearchivos)

---

## Variables

 - Las variables deben escribirse con snake_case
 - El nombre de la variable debe ser otorgado por la información que alamacena

   
 - En la declaracion de la misma debe tener un espacio entre el igual, el nombre y el dato

**Código esperado:**

```python
nombre_de_usuario = "Pedro"
```

**Evitar:**

```python
nombredeusuario="Pedro"
```

---

## Funciones ## 

- Las funciones al igual que las variables mantienen el snake_case

- Debajo de cada funcion (después de su declaración) debe haber un comentario que explique que operación realiza, argumentos que recibe y valores que devuelve

- El nombre de la función debe ser autoexplicativo

  **Código esperado:**

  ```python
  def suma(num:int, num2:int):
      """
      Description:
      	Esta función recibe dos números y devuelve la suma de los mismos
      Args:
      	num: Uno de los números de la operación
      	num2: Otro número entero
      Return:
      	La suma de los números
      """
      return num + num2
  ```

  **Evitar:**

  ```python
  def mondongo123(w, a):
      return w-a
  ```

  ## Clases ##

  - Los nombres de las clases deben escribirse en PascalCase

  - Los nombres de los métodos deben escribirse con snake_case, lo mismo aplica para los atributos

  - Cada método debe contener la misma descripción después de la declaración que una función

    ## Código esperado ##

    ```python
    class MrStickman:
        """
        Description:
        	El MrStickman va a hablar con las personas y tiene cancer terminal
        """
        def __init__(self, name:str, enfermedad:Dict, extremidades:int):
            self.name = nombre
            self.enfermedad = enfermedad
            self.extremidades = extremidades
        def saludar(self,words:str):
            """
            Description:
            	MrStickman va a decir lo que el usuario quiera
            Args:
            	words: Lo que quieras que diga MrStickman
            """
            print(f"MrStickman dice {words}")
    ```

    ## Evitar ##

    ```python
    class mrstickman:
    
        def __init__(si, name:str, no:Dict, tal_vez:int):
            self.name = nombre
            self.enfermedad = enfermedad
            self.extremidades = extremidades
        def saludar(self,words:str):
            
            print(f"MrStickman dice {words}")
    ```

    

