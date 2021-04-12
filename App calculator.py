#created by pradelson francois on 11/4/2021
from tkinter import *

tk = Tk()

#programando la operación de la suma
def fnsuma():
  n1 = texto1.get()
  n2 = texto2.get()
  r = float(n1) + float(n2)
  texto3.delete(0,"end")
  texto3.insert(0,r)

#programando la operación de la divición
def fndividir():
  n1 = texto1.get()
  n2 = texto2.get()
  r = float(n1) // float(n2)
  texto3.delete(0,"end")
  texto3.insert(0,r)

#programando la operación de la resta
def fnrestar():
  n1 = texto1.get()
  n2 = texto2.get()
  r = float(n1) - float(2)
  texto3.delete(0,"end")
  texto3.insert(0,r)   


tk.title("my app")

#configurando las dimensiones de la ventana
tk.geometry("600x600")

#Texto para escribir los números  
Lbl1 = Label(tk, text = "Primer número", bg = "yellow")
Lbl1.place(x=10, y=10, width=130, height=30)

#Campo de texto para que el usuario digite los numeros
texto1 = Entry(tk, bg = "white")
texto1.place(x=150, y=10, width=130, height=30)


Lbl2 = Label(tk, text = "Segundo número", bg = "yellow")
Lbl2.place(x=12, y=50, width=130, height=30)

#boton para realizar operaciones para sumar
botton1 = Button(tk, bg = "cyan", text = "Sumar", command = fnsuma)
botton1.place(x=300, y=50, width=100, height=30)

#boton para realizar operaciones para dividir
botton2 = Button(tk, bg = "orange", text = "Divición", command = fndividir)
botton2.place(x=300, y=110, width=100, height=30)

#boton para realizar operaciones para restar
botton3 = Button(tk, bg = "green", text = "Resta", command = fnrestar)
botton3.place(x=300, y=160, width=100, height=30)

texto2 = Entry(tk, bg = "white")
texto2.place(x=150, y=50, width=130, height=30)

Lbl3 = Label(tk, text = "Resultado", bg = "yellow")
Lbl3.place(x=14, y=110, width=100, height=30)

texto3 = Entry(tk, bg = "pink")
texto3.place(x=150, y=110, width=130, height=30)

tk.mainloop()

