n = int(input("¿Cuántos datos deseas ingresar? "))
datos = []
contador = 0

while contador < n:
    valor = float(input("Ingresa el valor: "))
    datos.append(valor)
    contador += 1

indice = 0
suma = 0
maximo = datos[0]
minimo = datos[0]
positivos = 0
negativos = 0
ceros = 0

while indice < n:
    valor = datos[indice]
    suma += valor

    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        ceros += 1

    indice += 1

promedio = suma / n

print("\nResultados del análisis:")
print("Datos ingresados:", datos)
print("Suma total:", suma)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
print("promedio:", promedio)
print("valor maximo:", maximo)
print("valor minimo:", minimo)
print("cantidad de positivos:", positivos)
print("cantidad de negativos:", negativos)
print("cantidad de ceros:", ceros)