import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        for store in self._model.getAllStores():
            self._view._ddStore.options.append(ft.dropdown.Option(store.store_name))
            self._view.update_page()





    def handleCreaGrafo(self, e):
        store= self._view._ddStore.value
        self._model.buildgraph(store.store_id)
    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
