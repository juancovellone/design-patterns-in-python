# Descriptor (Descriptor) 

## Categoría
* Comportamiento

Se clasifica como un patrón de comportamiento.
## Motivación
Este patrón se utiliza para personalizar el comportamiento de los atributos de una clase.


## Aplicabilidad
Cualquier objeto que al momento del set, get o delete deba realizar un comportamiento específico y 
este comportamiento lo tengamos encapsulado en un descriptor para su re utilización.

## Ejemplo
Supongamos que tenemos un clase que tiene uno o varios atributos que se tienen que guardar siempre
en minúscula, no importa como lo ingreso el usuario.

Se podría utilizar un *Descriptor* que maneje este comportamiento y nos quedaría encapsulado para poder utilizar lo 
en otros atributos de cualquier clase.

Si bien este comportamiento se puede manejar dentro de los métodos get y set, si es un comportamiento repetitivo, el descriptor
nos ayudaría a encapsular ese comportamiento.

**Aclaración**: Si se utiliza python <= 3.4 elimine el Typing.
