import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._product = DAO.getAllProduct()
        self._grafo = nx.Graph()
        self._idMapProduct = {}
        for p in self._product:
            self._idMapProduct[p.Product_number] = p

    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._product)

    def allEdges(self,colore):
        allEdges = DAO.getAllEdges(colore)
        for edges in allEdges:
            u = self._idMapProduct[edges[0]]
            v = self._idMapProduct[edges[1]]
            peso = self._idMapProduct[ edges[2]]
            self._grafo.add_edge(u,v,weight=peso)




