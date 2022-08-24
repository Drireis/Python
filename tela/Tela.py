from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen


class Tela1(ScrollView):
    pass


class MDIcon(MDScreen):
    pass


class Grid(MDGridLayout):
    pass


class Galeria(MDApp):
    def build(self):
        Builder.load_file("tela1.kv")
        return Tela1()



Galeria().run()
