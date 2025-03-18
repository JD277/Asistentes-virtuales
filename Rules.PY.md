 # Guia para hacer contribuciones al repositorio 

 ## Resumen

 Este es un resumen


---
 ## Tabla de contenidos

 1. Variables
 2. Funciones
 3. Clases
 4. Separacion de bloques de codigo 
 5. Archivos y organización

---

 ## Variables
 - Las variables deben escribirse con snake_case.
 - El nombre de la variable debe ser otorgado por la informacion que guarda.
 - En la declaracion de la misma debe tener un espcio entre el igual, el nombre y el dato.


 **Código esperado:**
```py
 nombre_de_usuario = "Pedro"
```

**Evitar**:

```py
nombredeusuario="pedro"
```

---

## Funciones

- Las funciones al igual que las variables mantienen el snake_case

- Debajo de cada función (después de su declaracion) debe haber un comentario Pydoc que explique que operacion

   realiza, argumentos que recibe y valores que devuelve 

- El nombre de la función debe ser auto explicativo

   **Código esperado:** 

   

   ```python
   def suma(num:int,num2:int):
       """
       Description:
       	Esta funcion recibe dos numeros y devuelve la suma de los mismos
       Args:
       	num: Uno de los numeros que de la operación
       	num2: Otro número entero
       return:
       	la suma del los dos numeros
       """
       return num + num2
   ```

​	**Evitar:**

   ```python
	def arepa32(w, a):
		return w-a
   ```

---

## Clases 

- Los nombres de las clases deben escribirse con PascalCase.
- Los nombres de los métodos deben escribirse con snake_case, lo mismo aplica para los atributos.
- Cada método debe contener la misma descripción después de la declaración que una función.

​	**Código esperado:**

```py
class MrStickman:
    """
    Description:
    	El MrStickman va a hablar con las personas y tiene cancer terminal
    	
    """
    def __init__(self, name:str, enfermedades:Dict, extremidades:int):
        self.name = nombre
        self.enfermedad = enfermedad
        self. extremidades = extremidades
    def saludar(self,words:str):
        """
        Description:
        	MrStickman va a decir lo que el usuario quiera
        args:
        	words: lo que quieres que diga MrStickman 
        """
        print(f"MrStickman dice {words}")
```

​	**Evitar:**

```python
class MrStickman:

    def __init__(self, name:str, enfermedades:Dict, extremidades:int):
        self.name = nombre
        self.enfermedad = enfermedad
        self. extremidades = extremidades
    def saludar(self,words:str):
     
```

