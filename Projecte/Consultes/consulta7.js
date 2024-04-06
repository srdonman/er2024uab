db.Productes.aggregate([
    {
      $group: { _id: "$categoria", 
      productes: {$push: "$$ROOT"}}
    }
  ])
  