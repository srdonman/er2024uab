db.Tiquets.aggregate([
    {$match: {productes: "Escaire"}},
    {$project: {"_id": 0, "Nom": "$client.Nom", "Cognom": "$client.Cognom"}}])
