print("\nEjercicio 3: ¿Cuanto escucho a mi artista favorito?")
print("\nMI ARTISTA FAVORITO\n")

artista = "Drake"
canciones_por_dia = 25
duracion_promedio = 3.5  # minutos por cancion

minutos_dia = canciones_por_dia * duracion_promedio
minutos_anio = minutos_dia * 365
horas_anio = minutos_anio / 60
dias_anio = horas_anio / 24

print(f"Escuchas a {artista} {minutos_dia} minutos al dia")
print(f"Al año son {minutos_anio} minutos")
print(f"¡0 sea {dias_anio:.1f} dias completos escuchando a {artista}!\n")
