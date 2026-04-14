import json

def exportar_a_json(lista_clientes, archivo="database/reporte_clientes.json"):
    """Serializa los objetos de clientes a un formato JSON."""
    datos = []
    for c in lista_clientes:
        dict_cliente = {
            "id": c.id_cliente,
            "nombre": c.nombre,
            "email": c.email,
            "tipo": getattr(c, 'tipo', 'Regular')
        }
        datos.append(dict_cliente)
    
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)
    print(f"📂 Datos exportados a {archivo}")