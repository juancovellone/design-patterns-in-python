# Adapter (Adaptador) 

## Categoría
* Estructurala

Los patrones estructurales se enfocan en la composición de clases y objetos para formar estructuras.


## Motivación
El patrón Adapter específicamente se utiliza para adaptar una interfaz existente a otra interfaz que se espera o se necesita.

## Aplicabilidad
Es recomendable utilizar el patrón adaptador cuando:
* Se desea usar una clase existente, y su interfaz no sea igual a la necesitada.
* Cuando se desea crear una clase reutilizable que coopere con clases no relacionadas. Es decir, que las clases no tienen necesariamente interfaces compatibles.
## Ejemplo
Supongamos que utilizamos una librería en nuestro código que retorna ciertos datos. 
Por alguna razón dicha librería queda sin soporte y necesitamos utilizar otra que sigue teniendo soporte y realiza las mismas
acciones, pero sus métodos se llaman distintos. En este caso se puede usar un *Adapter* y que la nueva librería se adapte 
a nuestro código sin la necesidad de cambiar en todos lados los llamados a los métodos.

En este ejemplo vamos a tener una clase OldLibrary que tiene un método get_description y retorna la descripción 
y la nueva librería tiene se llama NewLibrary y tiene un método description que returna un diccionario con la clave description y la descripción.
El adaptador debe adapatar la nueva clase para que se pueda llamar a un metodo get_description y retorne la descripción.

**Aclaración**: Si utiliza python <= 3.4 elimine el Typing.
