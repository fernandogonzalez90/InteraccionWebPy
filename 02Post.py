import requests
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Selecciona el archivo.')
parser = parser.parse_args()

if parser.file:
    if path.exists(parser.file):
        archivo = open(parser.file, 'rb')
        headers = {'User-Agent' : 'Firefox'}
        # Crear un input para ingresar la url completa y asi subir archivos a cualquier web.
        peticion = requests.post(url='http://feremagon.tk/uploader.php', files={'uploaded_file':archivo}, headers=headers)
        if parser.file in peticion.text:
            print(peticion.text)
            print('Archivo subido exitosamente.')
        else:
            print('Fallo la carga del archivo.')
    else:
        print('No existe e larchivo')
else:
    print('Tienes que seleccionar un archivo.')