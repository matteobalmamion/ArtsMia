import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"il grafo contiene {self._model.getNumEdges()} archi"))
        self._view.update_page()

    def handleCercaPercorso(self,e):

        self._model.getBestPath(int(self._view._ddLun.value),self._model.getObjectFromID(self._view.txtIdOggetto.value))

    def handleCompConnessa(self,e):
        idAdded=self._view._txtIdOggetto.value
        try :
            intID=int(idAdded)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è consono"))
            self._view.update_page()
            return
        if self._model.checkExistance(intID):
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intID} è presente nel grafo"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intID} non è presente nel grafo"))
        sizeConnessa=self._model.getConnessa(intID)
        self._view.txt_result.controls.append(ft.Text(f"La componenete connessa che contiene {intID} ha dimensione {sizeConnessa}"))
        myOpt=list(range(2,sizeConnessa))
        for i in myOpt:
            self._view._ddLun.options.append(ft.dropdown.Option(i))
        self._view.update_page()
