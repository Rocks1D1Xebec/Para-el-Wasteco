n=6
bus=1
estrella=n
anillo=n

malla_completa=n*(n-1)//2
print('Nodos:',n)
print('Bus:',bus, 'medio compartido')
print('Estrella:',estrella, 'enlace hacia el centro')
print('Anillo:',anillo, 'enlaces')
print('Malla Completa:',malla_completa, 'enlaces')

red={
    'S': ['PC1', 'PC2', 'PC3', 'PC4'],
    'PC1': ['S'],
    'PC2': ['S'],
    'PC3': ['S'],
    'PC4': ['S']
}
for nodo, vecinos in red.items():
    print(nodo, 'tiene grado', len(vecinos))

red={
    'S': ['PC1', 'PC2', 'PC3'],
    'PC1': ['S'], 'PC2': ['S'], 'PC3': ['S'],
}

fallo='S'
red_sin_fallo={n:[v for v in vs if v != fallo] for n,vs in red.items() if n != fallo}

visitados=set()
pendientes=['PC1']
while pendientes:
    actual=pendientes.pop()
    if actual not in visitados:
        visitados.add(actual)
        pendientes += red_sin_fallo.get(actual, [])

print('Nodos alcanzables:', visitados)
print('Red es conectada:', len(visitados) == len(red_sin_fallo))


nodos=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6']
origen='PC1'
destino='PC5'

i=nodos.index(origen)
j=nodos.index(destino)

horario=(j-i) % len(nodos)
antihorario=(i-j) % len(nodos)

print('Saltos por sentido horario:', horario)
print('Saltos por sentido antihorario:', antihorario)
print('Ruta mas corta:', min(horario, antihorario), 'saltos')


grados=[1,1,1,1,4]
n=len(grados)

if grados.count(1) == n-1 and max(grados) == n-1:
    print('Probable tecnologia: Estrella')
elif all(g == 2 for g in grados):
    print('Probable tecnologia: Anillo')
elif max(grados) > 2 and min(grados) == 1:
    print('Probable tecnologia: Malla Completa')
else:
    print('Topologia no identificada con esta regla simple')


topologias={
    'bus': 'si falla el medio principal, cae la red',
    'estrella': 'si falla el switch, cae la red',
    'anillo': 'si se rompe el ciclo, puede interrumpirse la comunicacion'
}

for nombre, efecto in topologias.items():
    print(nombre.upper(), '->', efecto)