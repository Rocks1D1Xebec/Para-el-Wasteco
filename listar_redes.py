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
    print(dispositivo, '->', lista)

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

enlaces=[('R1', 'R2'), ('R2', 'R3'), ('R3', 'R4'), ('R4', 'R1'), ('R1', 'R3')]

def quitar_enlace(lista, enlace_caido):
    a, b=enlace_caido
    return [e for e in lista if e != (a,b) and e != (b,a)]

print('Enlaces originales:', enlaces)

nueva_red=quitar_enlace(enlaces, ('R1', 'R3'))
print('Despues de la falla:', nueva_red)
print('Cantidad de enlaces restantes:', len(nueva_red))

def clasificar_red(distancia_km, medio):
    if medio.lower() == 'wifi' and distancia_km <= 0.1:
        return 'WLAN'
    elif distancia_km<=1:
        return 'LAN'
    elif distancia_km<=50:
        return 'MAN'
    else:
        return 'WAN'

casos=[(0.05, 'WiFi'), (0.5, 'utp'), (15, 'fibra'), (700, 'fibra')]

for distancia, medio in casos:
    print(distancia, 'km', medio, '->', clasificar_red(distancia, medio))"""


def enlaces_estrella(n_hosts):
    return n_hosts
def enlaces_malla_completa(n_hosts):
    return n_hosts * (n_hosts - 1) // 2
for n in [4,5,6,10]:
    print('Nodos:', n)
    print('Estrella:', enlaces_estrella(n-1), 'enlaces')
    print('Malla completa:', enlaces_malla_completa(n), 'enlaces')
    print('---')