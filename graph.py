
class Vertex:
    def __init__(self, key ):
        self.id = key
        self.connectedto = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedto[nbr] = weight
    
    def getConnections(self):
        return self.connectedto.items()
    
    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedto[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices +=1

        newVertex = Vertex(key) #create vertex object 
        self.vertList[key] = newVertex #ok so a dictionary can hold objects
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, cost)
    
    def getVertices(self):
        return self.vertList.keys()

    def totalVertices(self):
        return self.numVertices
    
    #def __iter__(self):
       # return iter(self.vertList.values())



#g = Graph()

#g.addEdge(2,3)
#g.addEdge(4,5)

#for i in g.vertList.values():
   # for j in i.getConnections():
    #    print("{0} --> {1}".format(i.getID(), j.getID()))