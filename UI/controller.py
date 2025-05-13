import flet as ft

from database.DAO import DAO
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        anno = [2015,2016,2017,2018]
        for a in anno:
            self._view._ddyear.options.append(ft.dropdown.Option(a))

        colori = DAO.getAllColors()
        for c in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))





    def handle_graph(self, e):
        pass



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
