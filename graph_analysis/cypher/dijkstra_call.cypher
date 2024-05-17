MATCH (player1:Player {name: $player_1_name}), (player2:Player {name: $player_2_name})
WHERE player1 <> player2
CALL gds.shortestPath.dijkstra.stream('FootballTransfers', {
  sourceNode: player1,
  targetNode: player2,
  relationshipWeightProperty: 'distance'
})

YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path

RETURN index,
    gds.util.asNode(sourceNode).name AS sourceNodeName,
    gds.util.asNode(targetNode).name AS targetNodeName,
    totalCost,
    [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames,
    costs,
    nodes(path) as path
ORDER BY costs;