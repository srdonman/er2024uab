db.Productes.aggregate([
    {$group: {
            _id: null,
            Maxim: {$max: "$preu"},
            Minim: {$min: "$preu"},
            Mitja: {$avg: "$preu"}}}])
    