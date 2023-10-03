ventas=[
    {"id": "afc001",
    "nombre": "Alejandra", 
    "costo": 350000
    },
    {"id": "afc020",
    "nombre": "Mariana", 
    "costo": 215000
    },
    {"id": "afc012",
    "nombre": "Matias", 
    "costo": 542000
    },
    {"id": "afc025",
    "nombre": "Didier", 
    "costo": 352000
    }, 
    {"id": "afc018",
    "nombre": "Lina", 
    "costo": 685000
    },
    {"id": "afc018",
    "nombre": "Pedro", 
    "costo": 359000
    }
]

#que los id esten en mayuscula
convertirMayuscualas = lambda texto: texto.upper()

for venta in ventas:
    venta["id"] = convertirMayuscualas(venta["id"])


#obtener compras superiores a 600000
ventasSuperiores=[venta for venta in ventas if venta["costo"] > 600000]


#ordenar compras superiores de mayor a menor
ventasOrdenadas= sorted(ventas, key = lambda venta: venta["costo"])

for venta in ventasOrdenadas:
    print(f"{venta['id']}---{venta['nombre']} costo: {venta['costo']}")

