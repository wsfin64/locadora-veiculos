from tkinter import *

# ---------------------------- CLASSE MÃE PARA AS JANELAS DO APLICATIVO --------------------------------------------
# ---------------------------- MOTHER CLASS FOR ALL WINDOWS IN THE APP ---------------------------------------------


class Window:

    def __init__(self, master):

        self.__master = master
        self.__new = None

    def close(self):
        self.__master.destroy()

    def new_window(self, _class):
        self.__new = Toplevel(self.__master)
        _class(self.__new)
