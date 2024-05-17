CALL gds.louvain.write(
         'CountryTransfersV3',
         {writeProperty:'community_number',
          maxIterations: 15,
          maxLevels: 15
          }) 

MATCH (source)-[r:PLAYED_FOR | PLAYS_IN | WITHIN]->(target) 
WHERE (source:Country or source:Club or source:Player) and (target:Country or target:Club or target:Player)
            WITH gds.graph.project(
                'CountryTransfersV3',
                source,
                target,
                {
                    sourceNodeLabels: labels(source),
                    targetNodeLabels: labels(target),
                    relationshipType: type(r)
                }
                ) AS g
            RETURN g.graphName AS graph, g.nodeCount AS nodes, g.relationshipCount AS rels

MATCH (n) WHERE (n.community_number) IS NOT NULL 
RETURN DISTINCT "node" as entity, n.community_number AS community_number, n AS node_ LIMIT 25 
UNION ALL 
MATCH ()-[r]-() WHERE (r.community_number) IS NOT NULL 
RETURN DISTINCT "relationship" AS entity, r.community_number AS community_number, 1 AS node_ LIMIT 25


MATCH (c:Country)
RETURN c.community_number AS country_community_number, COLLECT(c.name) AS country_names
ORDER BY country_community_number DESC


MATCH (c:Country), (comm:Community)
WHERE c.community_number = comm.number
MERGE (c)-[:BELONGS_TO]->(comm);


MATCH (c:Player)-[]-(c1:Club)-[]-(c3:Country) Return c,c1,c3