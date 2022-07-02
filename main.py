import tkinter
from tkinter import *
from tkinter import messagebox
from services import Users

users = Users()

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenido")

    Label(text="Acceso al sistema", bg="SteelBlue1", fg="white", width="300", height="3",font=("Calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", width="30",height="3", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", width="30",height="3", command=registrar).pack()
    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesión")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña",bg="SteelBlue1", fg="white", width="300", height="3",font=("Calibri",10)).pack() 
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry= Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry= Entry(pantalla1, textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión").pack()

def registrar():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registrarse")

    global nombre_usuario_entry
    global contrasena_usuario_entry

    nombre_usuario_entry=StringVar()
    contrasena_usuario_entry=StringVar()

    Label(pantalla2, text="Por favor ingrese usuario y contraseña",bg="SteelBlue1", fg="white", width="300", height="3",font=("Calibri",10)).pack()
    Label(pantalla2, text="").pack

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry= Entry(pantalla2,textvariable=nombre_usuario_entry)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasenausuario_entry= Entry(pantalla2,textvariable=contrasena_usuario_entry)
    contrasenausuario_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=insertar_datos).pack()

def insertar_datos():
    nombre=nombre_usuario_entry.get()
    contrasena=contrasena_usuario_entry.get()
    users.insert_data_user(nombre,contrasena)
    messagebox.showinfo(message="Registro Exitoso", title="Aviso")

menu_pantalla()    