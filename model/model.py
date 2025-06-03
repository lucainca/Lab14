import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allStore=[]
        self._allNodes=[]
        self._grafo= nx.DiGraph()
        self._idMap= {}
        self._allEdges=[]
        for a in self._allNodes:
            self._idMap[a.order_id] = a



    def buildGraph(self,storeid,k):

        self._allNodes = DAO.getAllNodes(storeid)
        self._grafo.add_nodes_from(self._allNodes)
        self._allEdges = DAO.getAllEdges(self._idMap,storeid,k)
        for e in self._allEdges:
            if e.peso >0:
                self._grafo.add_edge(e.o1, e.o2, weight=e.peso)


    def getAllStores(self):
        self._allStore= DAO.getAllStore()
        return self._allStore

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getNumEdges(self):
        return self._grafo.number_of_edges()