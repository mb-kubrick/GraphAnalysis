import os
def run_louvain(driver):
    """Builds the graph from the supplied JSON data."""
    file_path = os.getcwd() + '/graph_analysis/cypher/louvain.cypher'
    # file_names = ['clean_database.cypher', 'build.cypher']
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    with driver.session() as session:
        result = session.run(query)