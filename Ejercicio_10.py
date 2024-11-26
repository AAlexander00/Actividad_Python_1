primerTiempo = float(input("ingrese el tiempo en minutos del dia 1: "))
primeraDistancia = float(input("Ingrese la distancia en metros del dia 1:"))
segundTiempo = float(input("ingrese el tiempo en minutos del dia 1: "))
segundaDistancia = float(input("Ingrese la distancia en metros del dia 1:"))
tercerTiempo = float(input("ingrese el tiempo en minutos del dia 1: "))
terceraDistancia = float(input("Ingrese la distancia en metros del dia 1:"))
tiempoTotal = primerTiempo + segundTiempo + tercerTiempo
distanciaTotal = primeraDistancia + segundaDistancia + terceraDistancia
PromedioTiempo = tiempoTotal / 3
promedioDistancia = distanciaTotal / 3
print(f"\nTotal del tiempo de entrenamiento: {tiempoTotal} minutos.")
print(f"Total de distancia recorrida: {distanciaTotal} metros")
print(f"Promedio de tiempo por día: {PromedioTiempo} minutos")
print(f"Promedio de distancia por día: {promedioDistancia} metros")