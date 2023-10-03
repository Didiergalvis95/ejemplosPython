salarios = [1160000, 2500000, 3200000, 6000000, 500000, 20000000, 2800000, 2000000, 3500000, 1200000]

#funcion lambda para organizar datos de mayor a menor
datosOrdenados = sorted(salarios, key = lambda salario: -salario)

print(datosOrdenados)