print("\nEjercicio 2: Mi mascota en años humanos")
print("\nMI MASCOTA")

nombre_mascota = "mochi"
tipo = "chihuahua"
edad_mascota = 5

# Rgela popular: 1 año de perro aquivale a 7 años humanos
edad_humana = edad_mascota * 7

# f-string: la f permite usar {variables} dentro del texto 
print(f"Mi {tipo} se llama {nombre_mascota}")
print(f"Tiene {edad_mascota} años de {tipo}")
print(f"¡En años humanos tendria {edad_humana} años!\n")
