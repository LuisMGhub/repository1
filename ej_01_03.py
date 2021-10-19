# Ejercicio 1 capitulo 3
hrs = input("Introduce Horas: ")
tarifa = input("Introduce Tarifa: ")
salario = (float(hrs))*(float(tarifa))
# Se realiza un aumento en las horas al trabajar mas de 40 horas
if float(hrs) > 40 :
    aumento = (float(hrs)-40)*(float(tarifa)*1.5)
    salario = (float(tarifa)*40)+(aumento)
print("Salario:", salario)
