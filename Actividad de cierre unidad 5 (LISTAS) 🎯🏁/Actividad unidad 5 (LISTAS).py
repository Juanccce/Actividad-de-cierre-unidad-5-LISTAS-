# TP 5 - Listas
# Juan Galati

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiples_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4:", multiples_de_4)

# 2) Mostrar el penúltimo elemento de una lista personalizada
cosas_favoritas = ["chocolate", "playa", "música", "películas", "gatos"]
print("2) Penúltimo elemento:", cosas_favoritas[-2])

# 3) Lista vacía, agregar tres palabras con append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3) Lista con append:", lista_vacia)

# 4) Reemplazar valores en lista "animales"
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista animales modificada:", animales)

# 5) [Este ejercicio requiere un análisis del código, no se brindó un programa para analizar]
print("5) El ejercicio 5 requiere un análisis de código específico, no se brindó uno en el PDF.")

# 6) Lista del 10 al 30 con saltos de 5, mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("6) Dos primeros números:", numeros[:2])

# 7) Reemplazar valores en la lista "autos"
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "focus"]
print("7) Lista autos modificada:", autos)

# 8) Crear lista "dobles" con el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista dobles:", dobles)

# 9) Modificaciones a la lista "compras"
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("9) Lista compras modificada:", compras)

# 10) Crear lista anidada según lo indicado
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10) Lista anidada:", lista_anidada)


















































































