# -*- coding: utf-8 -*-
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
plaçapk = bd['Plaçapk']

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

for key, value in dades.items():
    for doc in dades[key]:
        if key == 'Clients':
            clients.insert_one(doc)
        elif key == 'Cotxes':
            cotxes.insert_one(doc)
        elif key == 'Tiquets':
            tiquets.insert_one(doc)
        elif key == 'Productes':
            productes.insert_one(doc)
        else:
            plaçapk.insert_one(doc)

print(clients)



# Tanquem les connexions i el tunel
conn.close()