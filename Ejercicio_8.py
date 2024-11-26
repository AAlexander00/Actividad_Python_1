#Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al segundo operador.
# El cliente desea conocer el costo de cada llamada, El costo total de las llamadas a cada operador, y el
# total de las cuatro llamadas.

costoOperador1 = float(input("ingrese el costo por minuto del primer operador: "))
costoOperador2 = float(input("ingrese el costo por minuto del segundo operador: "))
costoLlamada1Operador1 = costoOperador1 * float(input("Ingrese la duracion de la primera llamada al operador 1 (en minutos): "))
costoLlamada2Operador1 = costoOperador1 * float(input("Ingrese la duracion de la segunda llamada al operador 1 (en minutos): "))
costoLlamada1Operador2 = costoOperador2 * float(input("Ingrese la duracion de la primera llamada al operador 2 (en minutos): "))
costoLlamada2Operador2 = costoOperador2 * float(input("Ingrese la duracion de la segunda llamada al operador 2 (en minutos): "))
costoTotaloperador1 = costoLlamada1Operador1 + costoLlamada2Operador1
costoTotaloperador2 = costoLlamada1Operador2 + costoLlamada2Operador2
costoTotal = costoTotaloperador1 + costoTotaloperador2
print(f"\nCostototal de las llamadas a cada operador: ")
print(f"Total de llamadas del operador 1: ${costoTotaloperador1}")
print(f"Total de llamadas del operador 2: ${costoTotaloperador2}")
print(f"\ncosto total de las cuatro llamadas: ${costoTotal}")