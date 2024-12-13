def guardarCurva(x,y,archivo_salida):
    with open(archivo_salida, mode="w") as archivo:
        archivo.write("x   y\n")
        for xi, yi in zip(x, y):
            archivo.write(f"{xi:<4}{yi}\n")
