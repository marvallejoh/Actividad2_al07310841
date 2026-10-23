print("\n+++++++++++++++++++++++")
print("Ejercicio 5 realizado por Mariana Vallejo\n")
print("Ejercicio 5: ¿Cuanto dura mi playlist?")

# Duracion de cada cancion en segundos
cancion1 = 145
cancion2 = 186
cancion3 = 240
cancion4 = 163
cancion5 = 241

# Sumamos todo
total_segundos = cancion1 + cancion2 + cancion3 + cancion4 + cancion5

# // division entera: cuantos minutos completos caben
minutos = total_segundos // 60

# % residuo: los segundos que sobran
segundos = total_segundos % 60
print("\nResultados")
print(f"Total en segundos: {total_segundos}")
print(f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print("\n++++++")