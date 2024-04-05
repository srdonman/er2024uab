db.Tiquets.aggregate([
    { $group: { _id: "$pagament", total_tiquets: { $sum: 1 }} }
])
