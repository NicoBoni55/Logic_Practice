# Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# No se pueden utilizar operaciones del lenguaje que
# lo resuelvan directamente.

def mayusculas(palabra):
    if(type(palabra) == str):

        palabras_mayuscula = []
        palabras = palabra.split(", ")
        for p in palabras:
            nueva_palabra = p[0].upper() + p[1:]
            palabras_mayuscula.append(nueva_palabra)

        print(" ".join(palabras_mayuscula))

mayusculas("chau loco que haces")
mayusculas("paz espero que te pases")
mayusculas("agujero")
mayusculas("loco")
mayusculas(9)