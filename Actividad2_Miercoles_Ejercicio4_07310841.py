print("\n----------------")
print("Ejercicio realizado por Mariana Vallejo\n")
print("Ejercicio 4: ¿cCuanto tardo en terminar una serie?")

# Damos de alta las variables
serie = "Bojack Horseman"
temporadas = 5
episodios_por_temporada = 12
minutos_por_episodio = 25
horas_al_dia = 4   #cuanto tiempo le dedico diario
# usamos las variables en las formulas
# total de episodios
total_episodios = temporadas * episodios_por_temporada

# total de minutos y horas
total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60

#¿cuantos dias necesito?
dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"{serie} tiene {total_episodios} episodios")
print(f"Son {total_minutos} minutos en total")
print(f"Equivale a {total_horas:.1f} horas")
print(f"Viendo {horas_al_dia} horas diarias, la terminas en {dias_necesarios:.1f} dias")
print("\n-----------------------------")
