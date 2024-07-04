from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'trabalho'))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result

# Inicializar a conexão com o banco de dados
db = Database("bolt://localhost:7687", "neo4j", "trabalho")

def init_db():
    global db
    db = Database("bolt://localhost:7687", "neo4j", "trabalho")
    print("Conexão com o banco de dados Neo4j foi bem-sucedida!")

def close_db():
    global db
    if db:
        db.close()
        db = None
        print("Conexão com o banco de dados Neo4j foi encerrada!")
