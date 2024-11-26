total = float(input("Ingrese el valor total de la herencia: "))
parteEsposa = total * 0.40
totalHerencia = total - parteEsposa
parteHijo1 = totalHerencia * 0.30
parteHijo2 = totalHerencia * 0.20
parteHijo3 = totalHerencia * 0.40
parteHijo4 = totalHerencia * 0.10
print(f"\nLa esposa recibe: ${parteEsposa}")
print(f"Hijo 1 recibe: ${parteHijo1}")
print(f"Hijo 2 recibe: ${parteHijo2}")
print(f"Hijo 3 recibe: ${parteHijo3}")
print(f"Hijo 4 recibe: ${parteHijo4}")