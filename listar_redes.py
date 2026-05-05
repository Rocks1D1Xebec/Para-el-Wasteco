"""
estrella=[('SW1', 'PC1'), ('SW1', 'PC2'), ('SW1', 'PC3'), ('SW1', 'PC4')]
arbol=[('Core', 'SW1'), ('Core', 'SW2'), ('SW1', 'PC1'), ('SW1', 'PC2'), ('SW2', 'PC3'), ('SW2', 'PC4')]

malla_parcial=[('R1', 'R2'), ('R2', 'R3'), ('R3', 'R4'), ('R4', 'R1')]

print(estrella)
print(arbol)
print(malla_parcial)

#=================================================

enlaces = [('SW1','PC1'), ('SW1','PC2'), ('SW1','PC3'),
('SW1','PC4')]

dispositivos = set()
for a, b in enlaces:
    dispositivos.add(a)
    dispositivos.add(b)

print('Cantidad de enlaces:', len(enlaces))
print('Cantidad de dispositivos:', len(dispositivos))
print('Dispositivos:', dispositivos)

#=================================================

enlaces = [('SW1','PC1'), ('SW1','PC2'), ('SW1','PC3'),
('SW1','PC4')]

grados = {}
for a, b in enlaces:
    grados[a] = grados.get(a, 0) + 1
    grados[b] = grados.get(b, 0) + 1

central = max(grados, key=grados.get)

print('Grados:', grados)
print('Nodo más conectado:', central)
print('Cantidad de conexiones:', grados[central])


enlaces = [('Core','SW1'), ('Core','SW2'), ('SW1','PC1'),
           ('SW1','PC2'), ('SW2','PC3'), ('SW2','PC4')]

vecinos = {}
for a, b in enlaces:
    vecinos.setdefault(a, []).append(b)
    vecinos.setdefault(b, []).append(a)

for dispositivo, lista in vecinos.items():
    print(dispositivo, '->', lista)"""

from collections import deque

enlaces = [('Core','SW1'), ('Core','SW2'), ('SW1','PC1'),
           ('SW1','PC2'), ('SW2','PC3'), ('SW2','PC4')]

vecinos = {}
for a, b in enlaces:
    vecinos.setdefault(a, []).append(b)
    vecinos.setdefault(b, []).append(a)

def buscar_ruta(origen, destino):
    cola = deque([[origen]])
    visitados = set()
    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]
        if nodo == destino:
            return ruta
        if nodo not in visitados:
            visitados.add(nodo)
            for v in vecinos.get(nodo, []):
                cola.append(ruta + [v])

print(buscar_ruta('PC1', 'PC4'))