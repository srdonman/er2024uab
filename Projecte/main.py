# -- coding: utf-8 --
from pymongo import MongoClient
import json
from options import Options

################################## PARAMETRES DE CONNEXIÓ ###################################

# En execució remota
Host = 'localhost'
Port = 8207

###################################### CONNEXIÓ ##############################################

DSN = "mongodb://{}:{}".format(Host, Port)

conn = MongoClient(DSN)

############################# TRANSFERÈNCIA DE DADES AMB MONGO ##############################

bd = conn['projecte']

clients = bd['Clients']
cotxes = bd['Cotxes']
tiquets = bd['Tiquets']
productes = bd['Productes']
plaçapk = bd['Plaçapk']

clients.drop()
cotxes.drop()
tiquets.drop()
productes.drop()
plaçapk.drop()

"""
Carregar les dades des d'un fitxer JSON
"""

# Obrir Fitxer JSON
# Parse options
opts = Options()
args = opts.parse()
if args.fileName is not None:
    with open(args.fileName, encoding='utf-8') as f:
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



# Tanquem les connexions i el tunel
conn.close()