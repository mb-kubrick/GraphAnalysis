CALL gds.graph.project(
    'FootballPlayerSimilarity',
    ['Player', 'League', 'Position', 'Club','Country'],
    ['PLAYS_AS', 'PLAYED_FOR', 'PLAYED_IN','PLAYS_FOR','PLAYS_IN', 'PART_OF', 'WITHIN']
)
YIELD
  graphName AS graph, nodeProjection, nodeCount AS nodes, relationshipProjection, relationshipCount AS rels