from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ListProperty

from kivy.core.window import Window

import mysql.connector
import re

import time

from kivy.uix.popup import Popup

class LoginScreen(GridLayout,App):
    conn = mysql.connector.connect(
            host = "localhost",
            port = "3306",
            user = "root",
            password = "YaelHugo2122",
            database = 'PIM'
        )
    cursor = conn.cursor()
    usuario = ''
    passw = ''

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2
        self.add_widget(Label(text='Usuario'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        btn = Button(text="Entrar")
        btn.bind(on_press=self.on_event)
        self.add_widget(btn)
        self.add_widget(Label(text='Contraseña'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        btn1 = Button(text='Crear una nueva cuenta')
        btn1.bind(on_press=self.on_touch)
        self.add_widget(btn1)

    def on_event(self,instance):
        var1 = self.username.text
        var2 = "'" + var1 + "'"
        var3 = self.password.text
        var4 = "'" + var3 + "'"
        sql = 'SELECT * FROM Usuarios WHERE Usuario = '
        sql1 = ' AND Contraseña = '
        sql2 = sql +  var2  + sql1 + var4 
        self.cursor.execute(sql2)
        record = self.cursor.fetchall()
        if record == []:
            content = Button(text='Cerrar!')
            popup = Popup(title='Usuario y/o contraseña incorrecto',content=content,size_hint=(None,None),size=(500,500))   
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        else:
            for row in record:
                self.usuario = row[1]
                self.passw = row[2]
            if var1 == self.usuario and var3 == self.passw:
                LoginScreen().run()
        
    def on_touch(self,instance):
        content = CreateAccountUser()
        popup = Popup(title='Para crear una cuenta, llena los siguientes recuadros',content=content,size_hint=(None,None),size=(600,600))
        content.btn1.bind(on_press=popup.dismiss)
        popup.open()

    def build(self):
        self.title='Pagina Principal'
        return FirstPage()

class CreateAccountUser(GridLayout):
    def __init__(self,**kwargs):
        super(CreateAccountUser,self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3
        self.add_widget(Label(text='Nuevo Usuario'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Nueva Contraseña'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        btn = Button(text="Registrar")
        btn.bind(on_press=self.on_event)
        self.add_widget(btn)

        self.btn1 = Button(text="Cerrar ventana")
        self.add_widget(self.btn1)

    def on_event(self,instance):
        var1 = self.username.text
        var2 = self.password.text
        self.username.text = ''
        self.password.text = ''
        
        self.var = 'Usuario: ' +  var1 + ', Contraseña: ' + var2 + ', presiona este boton para agregar al nuevo usuario'
        content = Button(text=str(self.var))
        popup = Popup(title='La informacion es correcta?',content=content,size_hint=(None,None),size=(1500,200))   
        content.bind(on_press=popup.dismiss)
        popup.open()


class FirstPage(GridLayout):
    def __init__(self,**kwargs):
        super(FirstPage,self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        
        btn1 = Button(text='Registrar nuevo objecto')
        btn1.bind(on_press=self.on_something)
        self.add_widget(btn1)

        btn2 = Button(text='Borrar un objeto existente')
        btn2.bind(on_press=self.on_touch)
        self.add_widget(btn2)

        btn3 = Button(text='Mostrar objetos en tiempo real')
        btn3.bind(on_press=self.on_peda)
        self.add_widget(btn3)

        btn = Button(text="Salir")
        btn.bind(on_press=self.on_event)
        self.add_widget(btn)

    def on_event(self,instance):
        exit()
    
    def on_peda(self,instance):
        time.sleep(5)
        content = Button(text='El articulo "Laptop DELL" ha sido removido de su ubicacion')
        popup = Popup(title='ALERTA!!!',content=content,size_hint=(None,None),size=(1000,200))
        popup.open()

    def on_something(self,instance):
        content = RegisterObject()
        popup = Popup(title='Para registrar un nuevo objeto, llena los siguientes recuadros',content=content,size_hint=(None,None),size=(800,800))
        content.btn1.bind(on_press=popup.dismiss)
        popup.open()

    def on_touch(self,instance):
        content = DeleteObject()
        popup = Popup(title='Para borrar un objeto existente, llena los siguientes recuadros',content=content,size_hint=(None,None),size=(800,800))   
        content.btn1.bind(on_press=popup.dismiss)
        popup.open()

class RegisterObject(GridLayout):
    def __init__(self, **kwargs):
        super(RegisterObject, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 7
        self.add_widget(Label(text='Nombre'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text='Modelo'))
        self.model = TextInput(multiline=False)
        self.add_widget(self.model)
        self.add_widget(Label(text='Costo'))
        self.cost = TextInput(multiline=False)
        self.add_widget(self.cost)
        self.add_widget(Label(text='Lugar en la casa'))
        self.place = TextInput(multiline=False)
        self.add_widget(self.place)
        self.add_widget(Label(text='Descripcion'))
        self.description = TextInput(multiline=False)
        self.add_widget(self.description)

        btn = Button(text="Registrar el nuevo objeto")
        btn.bind(on_press=self.on_event)
        self.add_widget(btn)

        self.btn1 = Button(text="Listo, cerrar esta ventana")
        self.add_widget(self.btn1)

    def on_event(self,instance):
        var1 = self.name.text
        var2 = self.model.text
        var3 = self.cost.text
        var4 = self.place.text
        var5 = self.description.text
        self.name.text = ''
        self.model.text = ''
        self.cost.text = ''
        self.place.text = ''
        self.description.text = ''

        self.var = 'El/la ' + var1 + ' de la marca ' + var2 + ' con valor de $' + var3 + ' colocada en el/la ' + var4 + ', ' + var5 + ', presionar para agregar'
        content = Button(text=str(self.var))
        popup = Popup(title='La informacion es correcta?',content=content,size_hint=(None,None),size=(1500,200))   
        content.bind(on_press=popup.dismiss)
        popup.open()

class DeleteObject(GridLayout):
    def __init__(self, **kwargs):
        super(DeleteObject, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 7
        self.add_widget(Label(text='Nombre'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text='Modelo'))
        self.model = TextInput(multiline=False)
        self.add_widget(self.model)
        self.add_widget(Label(text='Costo'))
        self.cost = TextInput(multiline=False)
        self.add_widget(self.cost)
        self.add_widget(Label(text='Lugar'))
        self.place = TextInput(multiline=False)
        self.add_widget(self.place)
        self.add_widget(Label(text='Descripcion'))
        self.description = TextInput(multiline=False)
        self.add_widget(self.description)


        btn = Button(text="Borrar objeto")
        btn.bind(on_press=self.on_event)
        self.add_widget(btn)

        self.btn1 = Button(text="Listo, cerrar esta ventana")
        self.add_widget(self.btn1)

    def on_event(self,instance):
        var1 = self.name.text
        var2 = self.model.text
        var3 = self.cost.text
        var4 = self.place.text
        var5 = self.description.text
        self.name.text = ''
        self.model.text = ''
        self.cost.text = ''
        self.place.text = ''
        self.description.text = ''

        self.var = 'El/la ' + var1 + ' de la marca ' + var2 + ' con valor de $' + var3 + ' colocada en el/la ' + var4 + ', ' + var5 + ', presionar para borrar'
        content = Button(text=str(self.var))
        popup = Popup(title='La informacion es correcta?',content=content,size_hint=(None,None),size=(1500,200))   
        content.bind(on_press=popup.dismiss)
        popup.open()

class MyApp(App):
    def build(self):
        self.title='Log in page'
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()