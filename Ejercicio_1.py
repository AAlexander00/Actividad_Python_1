Salario=int(input("ingrese su salario basico:"))
retencion=Salario*0.18
bonificacion=Salario*0.013
Salario_neto=(Salario-retencion)+bonificacion
print("El salario neto es:", Salario_neto)
print("El valor de la retencion es:", retencion)
print("La bonificacion fue de:",bonificacion)