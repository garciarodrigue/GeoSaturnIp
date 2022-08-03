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

print(Fore.CYAN +""" 
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
SaturIp

""")
azul = Fore.BLUE
rojo = Fore.RED
verde = Fore.GREEN
magenta = Fore.MAGENTA
negro =  Fore.BLACK
back = Back.BLACK
styl = Style.BRIGHT

time.sleep(4.0)
#>/dev/null &
#el input donde ira la ip victima
ip = input(str(styl + rojo + "Ingresa la Ip: " + verde ))
dirección_ip = ip;
#se guarda en la variable 


autenticacion = '06bdbdff-2e70-48b9-8b33-4e8565bfddac';
url = 'https://ipfind.co/?auth=' + autenticacion + '&ip=' + dirección_ip;
pedir = requests.get(url)
respuesta = json.loads(pedir.content)

os.system("mpv optenidos.mp3 >/dev/null &");
time.sleep(6.1)
print(" ")
Pais = styl + azul + "La Victima Es De: " + verde + respuesta['country']
for l in Pais:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Continen = styl + azul + "Continente de: " + verde + respuesta['continent']
for l in Continen:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Ciuda = styl , azul , "De La Ciudad De: " , verde , respuesta['city']
for l in Ciuda:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)


longitud = respuesta['longitude']
latitud =  respuesta['latitude']

#os.system("mpv cordenadas.mp3 >/dev/null &");

print("\n")
#print(Style.BRIGHT + Fore.RED + "La ultima Localizacion GPS Fue")
cordenadas = styl , azul , "Latitud " , verde , latitud , azul , " Longitude " , verde , longitud

for l in cordenadas:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(1.0)

print("\n")
print(styl + azul + "Locacion > " , verde , latitud ,  longitud )
print("\n")
time.sleep(1.0)

Region = styl , azul , "Codigo de Region: " , verde , respuesta['region_code']

for l in Region:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

Postal = styl , azul , "Codigo Postal: " , verde , respuesta['postal_code']

for l in Postal:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)

print("\n")
time.sleep(0.1)

lenguaje = styl , azul , "Idioma: " , verde , respuesta['languages']

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

print(styl , azul + "Moneda: " , verde , respuesta['currency'])




