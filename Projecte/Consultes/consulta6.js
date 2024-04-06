db.Productes.find({
    subproductes: {$exists: true},
    $expr: {$gt: [{$size: {$objectToArray: "$subproductes"}}, 4]}
  })
  