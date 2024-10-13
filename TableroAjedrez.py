def crear_tablero():
    # Crear un tablero de ajedrez 8x8
    tablero = []
    for i in range(8):
        fila = []
        for j in range(8):
            # Si la suma de i y j es par, la casilla es negra
            if (i + j) % 2 == 0:
                fila.append("⬛")
            else:
                fila.append("⬜")
        tablero.append(fila)
    return tablero

# Ejemplo de uso
tablero = crear_tablero()
for fila in tablero:
    print(" ".join(fila))












