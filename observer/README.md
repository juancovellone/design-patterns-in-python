# Observer (Observador) 

## Categoría
* Comportamiento

Se clasifica como un patrón de comportamiento porque cuando el objeto observable cambia de esto, 
notifica a todos sus observadores.

## Motivación
Si se necesita consistencia entre clases relacionadas, pero con independencia, es decir, con un bajo acoplamiento.


## Aplicabilidad
Cualquier objeto que deba notificar a otros por cambio de estado.

## Ejemplo
Supongamos una Revista Digital que desea notificar a sus suscriptores cada vez que hay una nueva publicación.
Dicha revista sería nuestro *Observable* y los suscriptores los *Observers*.
El Observable notifica a todos los observer con el Título, Descripción y la url de la nueva nota.

**Aclaración**: Si utiliza python <= 3.4 elimine el Typing.
