def guardarCurva(x,y,archivo_salida):
    with open(archivo_salida, mode="w") as archivo:
        archivo.write("SNR\tPe\n")
        for xi, yi in zip(x, y):
            archivo.write(f"{xi}\t{yi}\n")
