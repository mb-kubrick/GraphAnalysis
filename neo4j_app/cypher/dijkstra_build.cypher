CALL gds.graph.project.cypher(
    'FootballTransfers',
    'MATCH (n) RETURN id(n) AS id',
    'MATCH (n)-[e]-(m) RETURN id(n) AS source, e.distance AS distance, id(m) AS target'
);