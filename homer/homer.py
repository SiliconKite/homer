#!/home/pablo/anaconda2/bin/python
""" fdasfdasf """
import sys
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
import logging
from itertools import izip
#import date
import subprocess
import argparse
from datetime import datetime

url = 'www.milanuncios.com/venta-de-apartamentos-en-valencia-valencia/?desde=10000&hasta=100000&demanda=n&vendedor=part'
url = 'www.milanuncios.com/venta-de-apartamentos-en-valencia-valencia/?desde={}&hasta={}&demanda=n&vendedor=part'
cwd = os.getcwd()

args = sys.argv[1:]
parser = argparse.ArgumentParser(description='Welcome to Homer, el buscacasa')
parser.add_argument('-f', '--file', type=str, help='Offline, seleccionar html file, other options are ignored')
parser.add_argument('-l', '--last', action='store_true',help='Use last available downloaded html file')
parser.add_argument('-m', '--min',  type=int, default= 0 ,help='Precio minimo' )
parser.add_argument('-M', '--max',  type=int, default=100000, help='Precio maximo')
results = parser.parse_args(args)

if ( results.last ):
    #use latest downloaded file

    #ls = subprocess.Popen('ls *.html -tp'.split(), stdout=subprocess.PIPE)
    #ls = subprocess.Popen('ls -tp *.html'.split(), stdout=subprocess.PIPE)
    #head = subprocess.Popen('head -1'.split(), stdin=ls.stdout, stdout=subprocess.PIPE)
    #ls.stdout.close()
    #output = head.communicate()[0]
    #ls.wait()
    newest = max(glob.iglob('*.html'), key=os.path.getctime)
    FILENAME = cwd + '/' + newest
    print 'Using latest downloaded file : {}\n'.format(FILENAME)
elif (results.file):
    # TODO: check file exists ...
    FILENAME = cwd + '/' + results.file

else:
    # download site
    url = url.format(results.min,results.max)
    FILENAME = 'wget_url_min={}_max={}_{}.html'.format(results.min,results.max,datetime.now().strftime('%d-%m-%Y_%Hh%Mm%Ss'))
    FILENAME = cwd + '/' + FILENAME
    cmd = ['wget','--output-document={0}'.format(FILENAME),url]
    subprocess.call(cmd)

html_path = FILENAME
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

titulo = []
for tag in title_soup:
    titulo.append(tag.contents[0])

cuerpo = []
for tag in cuerpo_soup:
    cuerpo.append(tag.contents[0])

precio = []
for tag in precio_soup:
    precio.append(tag.contents[0])

# do some quick fixes to data
# set data properly
for t,p in izip(titulo,precio):
   print t,p


# Append titulo and list
property_dict = {k: v for k, v in izip(titulo, precio)}

      

