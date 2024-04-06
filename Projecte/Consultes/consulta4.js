db.Tiquets.aggregate([
    {$group: {_id: "$client",
    num_compres_cotxe: {$sum: "$cotxe"}}},
    {$match: { num_compres_cotxe: 0 }},
    {$limit: 5}])
