# importando biblioteca MDApp
from kivymd.app import MDApp
# importando lang Buider (construtor de tela),
from kivy.lang import Builder

# importando tkinter


# utilizar o lang KV
KV = '''

FloatLayout:
    orientation: 'vertical'

    MDFillRoundFlatButton:
        text: 'Acessar'
        text_color: 'black'
        size_hint_x: .2
        size_hint_y: .05
        pos_hint: {'center_x': .5, 'center_y': .2}
    MDIconButton:
        icon: "android"
        pos_hint:{"center_x": .5, "center_y": .85}
        user_font_size: "90sp"
    MDTextField:
        hint_text: 'E-mail:'
        size_hint_x: .4
        size_hint_y: .1
        pos_hint: {'center_x': .5, 'center_y': .6}
    MDTextField:
        hint_text: 'Senha:'
        size_hint_x: .4
        size_hint_y: .1
        pos_hint: {'center_x': .5, 'center_y': .5}    
    MDLabel:
        text: 'Esqueceu a senha?'
        pos_hint: {'center_y': .45}
        halign: 'center'
        theme_text_color: "Custom"
        text_color: 'black'
    MDTextButton:
        pos_hint: {'center_y': .35, 'center_x': .5}
        text: 'Recadastrar senha!'  

'''


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.accent_palette = 'Blue'
        return Builder.load_string(KV)


LoginApp().run()
