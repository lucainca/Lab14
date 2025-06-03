from database.DAO import DAO
from model.model import Model

mydao= DAO()
mymodel= Model()

#print(mydao.getAllStore())


mymodel.buildGraph(1, 5)
print(mymodel.getNumNodes())
print(mymodel.getNumEdges())
