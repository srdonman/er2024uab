db.Clients.find(
    {"Població": "Barcelona"},  
    {"_id": 0}).sort({"Edat": -1}).limit(1)
  