nivelAgua = int(input("Ingrese el nivel del agua: "))

if nivelAgua > 0 and nivelAgua <= 200:
    print(f"El nivel de agua es: {nivelAgua}, esta muy bajo")
elif nivelAgua > 200 and nivelAgua <= 400:
    print(f"El nivel de agua es: {nivelAgua}, esta operando con normalidad")
elif nivelAgua > 400:
    print(f"El nivel de agua es: {nivelAgua}, inicie plan de evacuación")
else:
    print(f"por favor revise el sensor de agua, {nivelAgua} nivel no valido")