	
import requests
from bs4 import BeautifulSoup
llamada = requests.get('https://www.starz.com/ar/es/')
print("El codigo de la llamada es ", llamada.status_code) 


# PELICULAS


datos_soup = BeautifulSoup(llamada.text, 'html.parser')

titulos = datos_soup.find_all("p",class_="title")
	
lanzamiento = datos_soup.find_all("p",class_="text-body")

sinopsis = datos_soup.find_all("p",class_="is-truncated")

	
# Declaramos listas vacias
lista_titulos = []
lista_lanzamiento = []
lista_sinopsis = []
 
# Guardamos los titulos en lista_titulos
for dato in titulos:
    lista_titulos.append(dato.find('a').get_text())
 
# Guardamos el año de lanzamiento en lista_lanzamiento
for dato in lanzamiento:
    lista_lanzamiento.append(dato.get_text())
 
# Guardamos la sinopsis en lista_sinopsis
for dato in sinopsis:
    lista_sinopsis.append(dato.get_text())
    
	

import pandas as pd 

df = pd.DataFrame({"titulos": lista_titulos, "lanzamiento": lista_lanzamiento,
                   "sinopsis": lista_sinopsis})
 
# removemos las /n del texto
df = df.replace('\n','', regex=True)
 
# removemos espacios multiples del texto
df = df.replace('\s+', ' ', regex=True)
 
# removemos espacios que esten al final o al principio del texto
df = df.apply(lambda x: x.str.strip())
 
#Imprimimos todas las lineas 
print(df.head())






# SERIES 

datos_soup = BeautifulSoup(llamada.text, 'html.parser')

titulos = datos_soup.find_all("p",class_="title")
	
episodios = datos_soup.find_all("div",class_="links flexgrid")

temporadas = datos_soup.find_all("div",class_="season-selector d-flex")

	
# Declaramos listas vacias
lista_titulos = []
lista_episodios = []
lista_temporadas= []
 
# Guardamos los titulos en lista_titulos
for dato in titulos:
    lista_titulos.append(dato.find('a').get_text())
 
# Guardamos los episodios en lista_episodios 
for dato in episodios:
    lista_episodios.append(dato.get_text())
 
# Guardamos las temporadas en lista_temporadas
for dato in temporadas:
    lista_sinopsis.append(dato.get_text())
    
	

 
df = pd.DataFrame({"titulos": lista_titulos, "episodios": lista_episodios,
                   "temporadas": lista_temporadas})
 
# removemos las /n del texto
df = df.replace('\n','', regex=True)
 
# removemos espacios multiples del texto
df = df.replace('\s+', ' ', regex=True)
 
# removemos espacios que esten al final o al principio del texto
df = df.apply(lambda x: x.str.strip())
 
#Imprimimos todas las lineas
print(df.head())
