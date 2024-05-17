CALL gds.graph.project(
  'ClubsTransfers', // graph name
  'Club', // node label
  {
    PLAYS_FOR: {
      type: 'PLAYS_FOR', // relationship type
      orientation: 'NATURAL' // since likes are mutual
    }
  }
);



