// Run Louvain Modularity algorithm 
CALL gds.louvain.stream('ClubsTransfers') 
YIELD nodeId, communityId 
WITH gds.util.asNode(nodeId) AS club, communityId 
MERGE (c:Community {id: communityId}) 
MERGE (club)-[:BELONGS_TO]->(c)

// Use WITH here to separate MERGE and MATCH
WITH club, communityId

MATCH (p:Player)-[:PLAYS_FOR]->(c1:Club)-[:BELONGS_TO]->(c:Community)
RETURN p, c1, c;