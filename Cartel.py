import matplotlib.pyplot as plt
import numpy as np

# Coordenadas del cubo
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])
aristas = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5),
           (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4)]

# Matrices de rotación
def matriz_rotacion(theta, eje):
    if eje == 'x':
        return np.array([[1, 0, 0],
                         [0, np.cos(theta), -np.sin(theta)],
                         [0, np.sin(theta), np.cos(theta)]])
    elif eje == 'y':
        return np.array([[np.cos(theta), 0, np.sin(theta)],
                         [0, 1, 0],
                         [-np.sin(theta), 0, np.cos(theta)]])

# Proyección
def proyectar(vertice, d=3):
    x, y, z = vertice
    z += d
    return [x / z, y / z]

# Animación
theta = 0
plt.figure(figsize=(6, 6))
while theta < 2 * np.pi:
    plt.clf()
    vertices_rotados = vertices @ matriz_rotacion(theta, 'x') @ matriz_rotacion(theta, 'y')
    proyectados = [proyectar(v) for v in vertices_rotados]
    for arista in aristas:
        coordenadas_x = [proyectados[arista[0]][0], proyectados[arista[1]][0]]
        coordenadas_y = [proyectados[arista[0]][1], proyectados[arista[1]][1]]
        plt.plot(coordenadas_x, coordenadas_y, 'bo-')
    plt.title("Proyección 2D de un cubo rotando en 3D")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.05)
    theta += np.pi / 60