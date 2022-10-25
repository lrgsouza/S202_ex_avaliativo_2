from db.database import Graph


class FamiliaDB:

    def __init__(self):
        self.db = Graph(uri='bolt://3.238.188.20:7687',
                        user='neo4j', password='history-copies-gardens')
    # ============================== CONSULTAS ===========================================
    def get_aposentado(self):
        return self.db.execute_query('MATCH (n:Aposentado) RETURN n.nome')
    def get_estudantes(self):
        return self.db.execute_query('MATCH (n:Estudante) RETURN n.nome')
    def get_falecidos(self):
        return self.db.execute_query('MATCH (n:Falecido) RETURN n.nome')
    def get_trabalhador(self):
        return self.db.execute_query('MATCH (n:Trabalhador) RETURN n.nome')

    def get_pets(self, fulano):
        return self.db.execute_query('MATCH (n:Pessoa {nome:$nome})-[:DONO_DE]-(p:Pet) RETURN p.nome',
                                     {'nome': fulano})
    def get_sons(self,fulano):
        return self.db.execute_query('MATCH (n:Pessoa )-[:FILHO_DE]-(p:Pessoa {nome:$nome}) RETURN n.nome',
                                     {'nome': fulano})
    def get_casado(self, fulano):
        return self.db.execute_query('MATCH (n:Pessoa {nome:$nome})-[j:CASADO_COM]-(p:Pessoa) RETURN p.nome, j.desde',
                                     {'nome': fulano})

    def get_AVOS(self, fulano):
        return self.db.execute_query('MATCH (n:Pessoa {nome:$nome})-[j:NETO_DE]-(p:Pessoa) RETURN p.nome',
                                     {'nome': fulano})