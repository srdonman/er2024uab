db.Cotxes.aggregate([
    {$match: {"estada.data_entrada": {
      "$gte": {"$date":"2024-04-11"},
      "$lt": {"$date":"2024-04-12"}}}},
    {$lookup: {
      from: "Clients",
      localField: "DNI_propietari",
      foreignField: "DNI",
      as: "client"}},
    {$unwind: "$client"},
    {$project: {
        _id: 0,
        "Plaça": {
        $concat: [{$toString: "$estada.pàrquing.Planta"}, " ", 
          "$estada.pàrquing.Zona"," ", 
          {$toString: "$estada.pàrquing.Numero"}," ",
          {$toString: "$estada.pàrquing.Carregador"}]},
        "Dades del vehicle": {
        "Matrícula": "$matrícula",
        "Marca": "$marca",
        "Model": "$model",
        "Tipus": "$tipus",
        "Color": "$color",
        "Distintiu Ambiental": "$distintiu_ambiental"},
        "Nom i Cognom del client": {
        $concat: ["$client.Nom", " ", "$client.Cognom"]}}}
        ])
