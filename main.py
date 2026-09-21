import json
import os
import time
import requests

"""
instalar los 2 últimos paquetes de arriba, sino no podrá ser ejecutado el script
instalar con comando pip en terminal:
pip install <paquete>
"""


def getInfoIP(ip):
    # Dos APIs, la primera es free (200xdia) y la otra es por token
    # API 1
    # _apiURL = 'https://api.db-ip.com/v2/free/'+ip
    # API 2
    # para obtener un token, crear su cuenta en https://ipinfo.io/
    token = 'coloca-aqui-tu-API-Token'
    _apiURL = 'https://ipinfo.io/' + ip + '/json?token=' + token

    r = requests.get(_apiURL)
    if r.status_code == 200:
        # print("sin errores")

        # Cargar informacion del consulta al diccionario
        parsed = r.json()

        # print(parsed)
        # print(type(parsed))
        # print(parsed["city"])

        # BLOQUE PARA API 1 - FREE 200querys x dia
        """
        inf1 = parsed["ipAddress"]  # IP Publica
        inf2 = parsed["countryName"]  # Pais
        inf3 = parsed["stateProv"]  # Provincia
        inf4 = parsed["city"]  # Ciudad

        linea_inf = inf1 + "|" + inf2 + "|" + inf3 + "|" + inf4
        print(f'IP Pública: {inf1}, País: {inf2}, Region: {inf3}, Ciudad: {inf4}')
        """
        # BLQOUE PARA API x TOKEN - FREE 50000querys x mes
        inf1 = parsed["ip"]  # IP Publica
        inf2 = parsed["country"]  # Pais
        inf3 = parsed["region"]  # Region
        inf4 = parsed["city"]  # Ciudad
        inf5 = parsed["org"]  # ISP

        linea_inf = inf1 + "|" + inf2 + "|" + inf3 + "|" + inf4 + "|" + inf5
        print(f'IP Pública: {inf1}, País: {inf2}, Region: {inf3}, Ciudad: {inf4}, ISP: {inf5}')
        # Primero imprimimos y luego enviamos la respuesta para ser grabada
        return linea_inf


if __name__ == '__main__':
    print("Comenzando captura de información")
    print("Leyendo información del listado listaIP.txt")
    # getInfoIP("210.37.175.230")

    # Ruta del listado de IP en TXT
    # list_path = 'D:/DEV/listaIP.txt'
    list_path = 'listaIP.txt'

    # Abrir en modo escritura el archivo de salida
    file = open("listado_output.txt", "w", encoding="utf-8")

    # indice
    i = 1

    # leemos el listado de IPs
    with open(list_path, encoding="utf-8") as f:
        # ip = f.readline()
        for linea in f:
            # Quitamos el salto de línea para dejar solo la IP
            ip = linea.rstrip()
            # Imprimimos el indice mas la informacion obtenida
            print(i, end=' ')
            # Escrbibimos los datos en el archivo
            file.write(getInfoIP(ip) + "\n")
            i += 1
            time.sleep(0.5)
    # Cerramos archivo de salida
    file.close()

    print("Ejecución finalizada, revisar archivo listado_output.txt en ruta del script")
