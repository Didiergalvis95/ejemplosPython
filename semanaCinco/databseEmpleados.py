empleados=[
    {"codigo": 105,
     "salario": 2000000,
     "nombre": "Fernando Fernadez"
    },
    {"codigo": 111,
     "salario": 3500000,
     "nombre": "Camilo Fernadez"
    },
    {"codigo": 120,
     "salario": 6450000,
     "nombre": "Alejandra Aristizabal"
    },
    {"codigo": 117,
     "salario": 2000000,
     "nombre": "Mariana Cuervo"
    },
    {"codigo": 103,
     "salario": 1800000,
     "nombre": "Matias Gonzales"
    },
    {"codigo": 101,
     "salario": 1500000,
     "nombre": "Ana Yepes"
    },
    {"codigo": 125,
     "salario": 4200000,
     "nombre": "Martha Garcia"
    },
    {"codigo": 112,
     "salario": 3200000,
     "nombre": "Didier Galvis"
    },
    {"codigo": 129,
     "salario": 2100000,
     "nombre": "Pedro Torres"
    }
]

#filtrar los empleados con salarios mayores a 2.5
empleadosSalariosAltos=[empleado for empleado in empleados if empleado["salario"] > 2500000]

print(empleadosSalariosAltos)

#se organicen por codigo de menor a mayor
empleadosPorCodigo = sorted(empleadosSalariosAltos, key = lambda empleado: empleado["codigo"])

for empleado in empleadosPorCodigo: 
    print(f"Codigo: {empleado['codigo']} --- Nombre: {empleado['nombre']}")