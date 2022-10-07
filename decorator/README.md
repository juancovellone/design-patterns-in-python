# Decorator (Decorador) 

## Categoría
* Estructural

Permite añadir dinámicamente funcionalidad a un objeto. Esto es util para no tener que crear sucesivas clases 
que heredan de la clase padre para añadir una funcionalidad.


## Aplicabilidad
* Añadir responsabilidades a objetos individuales de forma dinámica y transparente.
* Responsabilidades de un objeto pueden ser retiradas.
* Cuando la extensión mediante la herencia no es viable.
* Hay una necesidad de extender la funcionalidad de una clase, pero no hay razones para extenderlo a través de la herencia.
* Existe la necesidad de extender dinámicamente la funcionalidad de un objeto y quizás quitar la funcionalidad extendida.

## Ejemplo
Supongamos que tenemos una clase ApiClient que se encarga de hacer consultas a un servicio externo. 
Se puede dar caso que si tenemos varios ApiClients para distintos servicios, en algunas consultas podemos querer 
capturar un ToManyRequest y en otros quizás queremos propagar el error, podemos crear un decorador que capture dicha exepción y 
usar la en los casos que sean necesarios.

**Aclaración**: Si utiliza python <= 3.4 elimine el Typing.
