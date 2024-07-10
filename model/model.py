from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._artobjects=DAO.getAllObjects()
        self._grafo=nx.Graph()
        self._grafo.add_nodes_from(self._artobjects)
        self._idMap={}
        for v in self._artobjects:
            self._idMap[v.object_id]=v

    def creaGrafo(self):
        self.addEdges()

    def getConnessa(self,v0int):
        #Modo 1: successori di v0 in DFS
        v0=self._idMap[v0int]
        successors=nx.dfs_successors(self._grafo,v0)
        allSucc=[]
        for v in successors.values():
            allSucc.extend(v)
        print(f"Metodo 1 (prec): {len(allSucc)}")

        #Modo 2: predecessori di v0 in DFS
        pedecessor=nx.dfs_predecessors(self._grafo,v0)
        print(f"Metodo 2 (succ): {len(pedecessor.values())}")

        #Modo 3: conto i nodi dell'albero di visita
        tree=nx.dfs_tree(self._grafo,v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")

        #Modo 4: node_connected_component
        connComp=nx.node_connected_component(self._grafo,v0)
        print(f"Metodo 4 (connected component): {len(connComp)}")
        return len(connComp)

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def addEdges(self):
        #self._grafo.edges.clear()
        """ opzione 1 se ho pochi elementi
        for u in self._artobjects:
            for v in self._artobjects:
                peso=DAO.getPeso(u, v)
                self._grafo.add_edge(u, v, weight=peso)"""
        allEdges=DAO.getConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1,e.v2,weight=e.peso)

    def checkExistance(self,idOggetto):
        return idOggetto in self._idMap
