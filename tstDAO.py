from database.DAO import DAO
from model.model import Model

res=DAO.getAllObjects()
model=Model()
model.creaGrafo()
con=DAO.getConnessioni(model._idMap)
print(len(res))
print(len(con))