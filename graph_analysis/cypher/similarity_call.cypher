MATCH (player1:Player {name: $player_1_name}), (player2:Player {name: $player_2_name})
WHERE player1 <> player2
CALL gds.nodeSimilarity.filtered.stream('FootballPlayerSimilarity', {sourceNodeFilter:player1, targetNodeFilter:player2})
YIELD node1, node2, similarity
RETURN gds.util.asNode(node1).name AS Player1, gds.util.asNode(node2).name AS Player2, similarity
ORDER BY similarity DESCENDING, Player1, Player2