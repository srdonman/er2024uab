# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:53:42 2024

@author: 
"""


from pymongo import MongoClient
import json
from options import Options

################################## PARAMETRES DE CONNEXIÓ ###################################
mongoUser = ''
mongoPassword = ''
mongoDB = ''

"""
1.  Actualitzeu els paràmetres del script NoSQLfromPython.py per poder establir la connexió amb el MongoDB del vostre PC.
"""
# En execució remota
Host = 'localhost' 
Port = 27017


###################################### CONNEXIÓ ##############################################

DSN = "mongodb://{}:{}".format(Host,Port)

conn = MongoClient(DSN)


############################# TRANSFERÈNCIA DE DADES AMB MONGO ##############################

#Selecciona la base de dades a utilitzar --> test
bd = conn['projecte']

clients = bd['Clients']
cotxes = bd['Cotxes']
tiquets = bd['Tiquets']
productes = bd['Productes']
plaçapk = bd['plaçapk']

llista = [clients, cotxes, tiquets, productes, plaçapk]
"""
Carregar les dades des d'unfitxer JSON
"""
#Obrir Fitxer JSON
# Parse options
opts = Options()
args = opts.parse()
if args.fileName is not None:
    with open(args.fileName) as f:
        dades = json.load(f)

    #Mostrem els continguts de Dades
    # print(dades)

for index, classe in enumerate(dades): 
    for doc in dades[classe]:
        llista[index].insert_one(doc) 
print(clients)

# Tanquem les connexions i el tunel
conn.close()




