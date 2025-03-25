# Guia para hacer contribuciones al repositorio

## Resumen

Este es un resumen

---
## Tabla de conenidos 

1. [Variables](#variables)
2. [Funciones](#funciones) 
3. [Clases](#clases)
4. [Separacion de grandes bloques de codigo](#organizacion)
5. [Archivos y organizacion](#manejodearchivos)

---

## Variables
- Las variables deben escribirse consanke_case
- El nombre de la variable deve ser otorgado por la infirmacion que almacena
- En la declaracion de la misma debe tener un espacio entre el igual, el nombre y el dato

**Codigo esperado:**
```python
nombre: "pibe"
```

**Evitar**

```python
nombredeusuario:"padre"
```

## Funciones:

- Las funciones al igual que la variables mantienen el snake_case.

- Debajo de cada funcion(despues de su declaracion) debe haber un comentario Pydoc que esplique que operacion realiza, argumentos que recibe y valores que devuelva.

- El nombre de la funcion debe ser autoexplicativo. 

  **Codigo esperado**

```python
def suma(num: int,num2: int):
    """
    Descirption:
    	Esta funcion recibe dos numeros de la operacion
    Args:
    	num: Uno de los numeros de la operacion
    	num2: Otro numero entero
    Return:
    	La suma de los numeros
    """
    return num + num2
```

**Evitar:**

```
def resta(w, a):
	return w - a
```

---



## Clases

- Los nombres de las clases deben escribirse con PascaLCase.
- Los nombres de los metodos deben escribirse con snake_case, lo mismo aplica para los atributos.
- 