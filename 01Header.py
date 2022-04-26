import requests
import argparse

parser = argparse.ArgumentParser(description='Detector de Comandos')
parser.add_argument('-t', '--target', help='Valor')
parser = parser.parse_args()

if parser.target:
    try:
        url = requests.get(url=parser.target)
        header = dict(url.headers)
        for i in header:
            print(i + ' : '+ header[i])
    except:
        print('Error de conexion')
else:
    print('No especificaste nada.')