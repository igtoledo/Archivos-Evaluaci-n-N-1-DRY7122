import json
try:
    with open("myfile.json", 'r') as archivo:
        ourjson = json.load(archivo)
        print("Contenido del archivo JSON:")
        print(ourjson)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo")
