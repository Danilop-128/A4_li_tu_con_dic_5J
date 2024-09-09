
print("Ejemplo de listas")
arcoiris=["verde", "azul", "morado"]
print(arcoiris)
longitud=len(arcoiris)
print("Elementos que contiene la lista de arcoiris ", longitud)
print(f"Elementos que contiene la lista de arcoiris v2 {longitud}")
print("Accediendo a un elemento de la lista")
print(arcoiris[1])
print(f"elemento en la posicion 0 es {arcoiris[0]}")
print(f"El primer elemento del arcoiris es:", arcoiris[0])
print("Agregar un elemento a la lista")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)
print("Listar los elementos de la lista ciclo for")
for lopez in arcoiris:
    print(lopez)
