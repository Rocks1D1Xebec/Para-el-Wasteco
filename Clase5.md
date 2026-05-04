Topologia

Como se organizan/conectan los equipos en una red

form: distribucion de equipos y enlaces
comunicacion: camino por el que viajan los datos
Fallas: Que ocurre si un cable o equipo deja de funcionar
Escalabilidad: facilidad para crecer sin rediseñar todo

Topologia fisica
Describe cables puertos, equipos y ubicacion real
Responde: como estan conectados fisicamente
Ejmplo: PCs conectadas a un switch central

Topologia logica
Describe como circula la informacion
Responde: por donde viajan los datos
Ejemplo: una red fisica en estrella puede operar logicamente como bus en tecnologias antiguas


*Tres tipo de topologia*

Bus
__________
| | | | |
* * * * *

Estrella(el ruter al centro)


Anillo: circulo



Topologia bus:
Ventajas bajo costo inicial facil de entender poco cableado en redfes pequeñas

Desventajas:
Un fallo en el medio afecta a todos
dificil de diagnosticcar
bajo rendimiento si hay mucho trafico

idea clave
Medio compartido=dependencia alta del cable principal


Estrella

Ventajas
facil de administrar y amplicar 
si falla un cable de usuario, no cae toda la red

desventajas
fi falla el switch central se afecta toda la red
requiere mas cable de bus

idea clave
es la mas comun en redes lan modernas

anillo

Ventajas
flujo ordenado de transmision
puede evitar colisiones en diseños especificos

Desventajas
una falla puede interrumpir el circuito si no hay redundancia
agregar o quitar nodos puede ser mas delicado

idea clabe
la comunicacion sigue una secuencia entre vecinos


Grafo
Nodo=computadora, switcg router o servidor
enlace= cable, conexion inalambrica o vinculo logico
la topologia es el patron de nodos y enlaces


bus=1