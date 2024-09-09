print("Ejemplos de tuplas")
canciones=("Te amo", "El NoNoa", "Amor eterno")
print(canciones)

y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)

print(x)