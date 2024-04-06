db.Clients.find(
    {"CodiPostal": /^080/},  
    {"_id": 0}).sort({"Edat": -1}).limit(1)
  