import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Cuenta de inversión")
ventana.config(width=400, height=300)

etiqueta_inversion = ttk.Label(text="Introduce la cantidad de inversión:")
etiqueta_inversion.place(x=10, y=10)
etiqueta_anios = ttk.Label(text="Introduce los años de inversión:")
etiqueta_anios.place(x=10, y=40)
etiqueta_interes = ttk.Label(text="Introduce el interés de la inversión:")
etiqueta_interes.place(x=10, y=70)

input_inversion = ttk.Entry()
input_inversion.place(x=200, y=10, width=80)
input_anios = ttk.Entry()
input_anios.place(x=200, y=40, width=80)
input_interes = ttk.Entry()
input_interes.place(x=200, y=70, width=80)

boton_calcular = ttk.Button(text="Calcular")
boton_calcular.place(x=100, y=100)

etiqueta_monto = ttk.Label(text="El monto acumulado es:")
etiqueta_monto.place(x=10, y=130)
ventana.mainloop()
