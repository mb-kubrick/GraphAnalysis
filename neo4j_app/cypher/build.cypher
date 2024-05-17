WITH
$player_names AS players,
$positions AS positions,
$ages AS ages,
$origin_clubs AS origin_clubs,
$league_origin_clubs AS league_origin_clubs,
$country_origin_clubs AS country_origin_clubs,
$new_clubs AS new_clubs,
$league_new_clubs AS league_new_clubs,
$country_new_clubs AS country_new_clubs

UNWIND range(0, size(players) - 1) AS index

// DEFINE NODES
MERGE (player:Player {name: players[index], age: ages[index]})
MERGE (position:Position {name: positions[index]})
MERGE (origin_club:Club {name: origin_clubs[index]})
MERGE (league_origin_club:League {name: league_origin_clubs[index]})
MERGE (country_origin_club:Country {name: country_origin_clubs[index]})
MERGE (new_club:Club {name: new_clubs[index]})
MERGE (league_new_club:League {name: league_new_clubs[index]})
MERGE (country_new_club:Country {name: country_new_clubs[index]})

// DEFINE CONNECTIONS
MERGE (player)-[:PLAYS_AS {distance: 1}]->(position)
MERGE (player)-[:PLAYED_FOR {distance: 1}]->(origin_club)
MERGE (player)-[:PLAYED_IN {distance: 1}]->(league_origin_club)
MERGE (player)-[:PLAYED_IN {distance: 1}]->(country_origin_club)
MERGE (player)-[:PLAYS_FOR {distance: 1}]->(new_club)
MERGE (player)-[:PLAYS_IN {distance: 1}]->(league_new_club)
MERGE (player)-[:PLAYS_IN {distance: 1}]->(country_new_club)

MERGE (origin_club)-[:PART_OF {distance: 1}]->(league_origin_club)
MERGE (origin_club)-[:WITHIN {distance: 1}]->(country_origin_club)

MERGE (new_club)-[:PART_OF {distance: 1}]->(league_new_club)
MERGE (new_club)-[:WITHIN {distance: 1}]->(country_new_club)

MERGE (league_origin_club)-[:WITHIN {distance: 1}]->(country_origin_club)
MERGE (league_new_club)-[:WITHIN {distance: 1}]->(country_new_club)
;