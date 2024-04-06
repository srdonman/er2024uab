db.Tiquets.aggregate([
    {$match: {"data": {
      "$gte": {"$date":"2023-04-01"},
      "$lte": {"$date":"2023-04-30"}}}},
    {$match: {preu_total: { $gt: 500 }}},
    {$count: "totalClients"}])
