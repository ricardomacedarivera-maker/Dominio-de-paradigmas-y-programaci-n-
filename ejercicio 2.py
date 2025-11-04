calificaciones = [85, 60, 78, 95, 97, 73, 70, 100, 34, 68, 80, 54]


for cal in calificaciones:
    if cal >= 60:
        print("Aprobado:", cal)
    else:
        print("Reprobado:", cal)


aprobados = 0
reprobados = 0
for cal in calificaciones:
    if cal >= 60:
        aprobados += 1
    else:
        reprobados += 1
print("Total de aprobados:", aprobados)
print("Total de reprobados:", reprobados)

maxima = calificaciones[0]
minima = calificaciones[0]
for cal in calificaciones:
    if cal > maxima:
        maxima = cal
    if cal < minima:
        minima = cal
print("La calificación más alta es:", maxima)
print("La calificación más baja es:", minima)


for cal in calificaciones:
    if cal % 2 == 0:
        print(cal, "es par")
    else:
        print(cal, "es impar")