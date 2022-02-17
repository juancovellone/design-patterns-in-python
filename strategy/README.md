# Strategy (Estrategia) 

## Categoría
* Comportamiento

Se clasifica como un patrón de comportamiento porque determina como se debe realizar el intercambio de mensajes entre 
diferentes objetos pare resolver la tarea.

## Motivación
Suponeos una calculadora con diferentes algoritmos para calcular las distintas operaciones, 
(suma, resta, multiplicacion, ...). 

Se desea separar las clases clientes por distintos motivos: 
* Incluir los algoritmos de los códigos (las operaciones) en el cliente hace que esto sean demasiados grandes y 
complicados de mantener y/o extender.
* El cliente no va a necesitar todos los algoritmos en todos los casos, de modo que no queremos que dicho cliente los 
almacene si no los va a usar.
* Si existiesen clientes distintos que usasen los mismos algoritmos, habría que duplicar el código, por tanto, esta 
situación no favorece la reutilización.

## Aplicabilidad
Cualquier programa que realice una tarea que pueda ser realizada de varias maneras es candidato a utilizar este patrón.
Puede haber 1 o infinitas estrategias y estas pueden en ser intercambiadas en cualquier momento, incluso en tiempo de 
ejecución.  Si muchas clases relacionadas se diferencian únicamente por su comportamiento, se crea una superclase Abstracta
que almacene el comportamiento común.

## Ejemplo
Se desea crear una calculadora simple, donde el contexto que es el que usa la estrategia en este caso sería la calculadora,
y esta por medio de distintas estrategias resuelve las operaciones.
Observar que en el caso de tener que crear otro tipo de calculadora que realice alguna o todas las mismas operaciones, 
sería muy sencillo de implementar y reutilizar código.

