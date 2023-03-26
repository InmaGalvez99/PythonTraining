barras_no_frescas = int(input("Introduzca el número de barras de pan no frescas"))
descuento = 0.60
precio = 3.49
coste = barras_no_frescas * precio * (1 - descuento)

print("El precio de una barra es", str(precio), "€")
print ( "El descuento a una barra no fresca es", str(descuento * 100), "%")
print("El coste final a pagar es",str(round(coste, 2)), "€" )
