#!/home/pablo/anaconda2/bin/python
""" fdasfdasf """
import os
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
import logging
from itertools import izip
#import date
import subprocess

url = 'http://www.milanuncios.com/venta-de-apartamentos-en-valencia-valencia/?hasta=100000&demanda=n&vendedor=part'

FILENAME = 'source.html'
cwd = os.getcwd()

# download site
#cmd = ['wget','--output-document={0}'.format(FILENAME),url]
# subprocess.call(cmd)

# Extract the shite out of this mofo
html_path = cwd + '/source.html'
soup = BeautifulSoup(open(html_path),'html.parser')
# anuncios_soup = soup.find_all("div", class_="aditem-detail")

# header de cada anuncio, de aqui sacamos ref y hora de actualizacion
# header_soup    = soup.find_all("div", class_="aditem-header display-desktop")

# timestamp
time_soup    = soup.find_all("div", class_="x6")
# reference
ref_soup    = soup.find_all("div", class_="x5")
# title del anuncio
title_soup    = soup.find_all("a", class_="aditem-detail-title")
# cuerpo del anuncio
cuerpo_soup   = soup.find_all("div", class_="display-desktop tx")
# precio
precio_soup   = soup.find_all("div", class_="aditem-price")


# Saca el actual text
time = []
for tag in time_soup:
    time.append(tag.contents)

ref = []
for tag in ref_soup:
    ref.append(tag.contents)

precio = []
for tag in precio_soup:
    precio.append(tag.contents[0])

titulo = []
for tag in title_soup:
    titulo.append(tag.contents[0])

# do some quick fixes to data
# set data properly

print precio
print titulo


# Append titulo and list
property_dict = {k: v for k, v in izip(titulo, precio)}
