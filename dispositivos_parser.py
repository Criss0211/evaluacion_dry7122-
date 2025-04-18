import json

data = []

with open('dispositivos.json','r') as file:
    dispositivos_data = json.load(file)

for i in dispositivos_data['dispositivos']:
        nombre = i['nombre']
        ip = i['ip']
        estado = i['estado']
        print(f"Nombre: {nombre}")
        print(f"  Dirección IP: {ip}")
        print(f"  Estado: {estado}")