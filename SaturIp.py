#!/usr/bin/env python
# -*- coding: utf-8 -*-
#aqui abajo importo Style
import os
import sys,time 
from colorama import Style,  Back, Fore, init
init()
#fin Style

#importamos metodos de datos y peticion
import json
import requests
#fin de importaciones

#limpio consola
os.system("clear")

print(""" 
                     .::.
                  .:'  .:
        ,MMM8&&&.:'   .:'
       MMMMM88&&&&  .:'
      MMMMM88&&&&&&:'
      MMMMM88&&&&&&
    .:MMMMM88&&&&&&
  .:'  MMMMM88&&&&
.:'   .:'MMM8&&&'
:'  .:'
'::'  T3NSHI

""")

#el input donde ira la ip victima
ip = input(str(Style.BRIGHT + Fore.RED + "Ingresa la Ip: " + Fore.GREEN ))
dirección_ip = ip;
#se guarda en la variable 


autenticacion = '06bdbdff-2e70-48b9-8b33-4e8565bfddac';
url = 'https://ipfind.co/?auth=' + autenticacion + '&ip=' + dirección_ip;
pedir = requests.get(url)
respuesta = json.loads(pedir.content)

print("\n")

Pais = Style.BRIGHT + Fore.BLUE + "La Victima Es De: " + Fore.GREEN + respuesta['country']
for l in Pais:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Continen = Style.BRIGHT + Fore.BLUE + "Continente de: " + Fore.GREEN + respuesta['continent']
for l in Continen:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Ciuda = Style.BRIGHT , Fore.BLUE , "De La Ciudad De: " , Fore.GREEN , respuesta['city']
for l in Ciuda:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

longitud = respuesta['longitude']
latitud =  respuesta['latitude']

print("\n")

print(Style.BRIGHT + Fore.RED + "La ultima Localizacion GPS Fue")

cordenadas = Style.BRIGHT , Fore.BLUE, "Latitud " , Fore.GREEN , latitud , Fore.BLUE , " Longitude " , Fore.GREEN , longitud


for l in cordenadas:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(1.0)

print("\n")
print(Style.BRIGHT + Fore.BLUE + "Locacion > " , Fore.GREEN , latitud ,  longitud )
print("\n")
time.sleep(1.0)

Region = Style.BRIGHT , Fore.BLUE , "Codigo de Region: " , Fore.GREEN , respuesta['region_code']

for l in Region:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Postal = Style.BRIGHT , Fore.BLUE , "Codigo Postal: " , Fore.GREEN , respuesta['postal_code']

for l in Postal:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

lenguaje = Style.BRIGHT , Fore.BLUE , "Idioma: " , Fore.GREEN , respuesta['languages']

for l in lenguaje:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")

nada = ""

for l in nada:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)


time.sleep(0.1)

print(Style.BRIGHT , Fore.BLUE + "Moneda: " , Fore.GREEN , respuesta['currency'])




