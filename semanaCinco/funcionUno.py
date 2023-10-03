def sumar(numeroUno, numeroDos):
    return numeroUno + numeroDos

#lambda
sumarAlternativo = lambda numeroUno, numeroDos: numeroUno + numeroDos 

#llamar funciones
resultado=sumar(5,10)
resultadoLamdba = sumarAlternativo(10,15)

print(resultado)
print(resultadoLamdba)