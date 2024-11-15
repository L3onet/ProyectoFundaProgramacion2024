import tkinter as tk
from tkinter import ttk
from cuentainversion import CuentaInversion

def calcularInversion():
    inversion = 0.0
    anios = 0.0
    interes = 0.0
    try:
        inversion = float(input_inversion.get())
        etiqueta_error_inversion.config(text=f"")
    except ValueError as ve:
        etiqueta_error_inversion.config(text=f"Introduce un número")
    try:
        anios = float(input_anios.get())
        etiqueta_error_anios.config(text=f"")
    except ValueError as ve:
        etiqueta_error_anios.config(text=f"Introduce un número")
    try:
        interes = float(input_interes.get())
        etiqueta_error_interes.config(text=f"")
    except ValueError as ve:
        etiqueta_error_interes.config(text=f"Introduce un número")
    montoFinal = CuentaInversion()    
    etiqueta_monto.config(text=f"El monto acumulado es: {montoFinal.calcularMontoAcumulado(inversion, anios, interes)}")

ventana = tk.Tk()
ventana.title("Cuenta de inversión")
ventana.config(width=500, height=300)

etiqueta_inversion = ttk.Label(text="Introduce la cantidad de inversión:")
etiqueta_inversion.place(x=10, y=10)
etiqueta_anios = ttk.Label(text="Introduce los años de inversión:")
etiqueta_anios.place(x=10, y=40)
etiqueta_interes = ttk.Label(text="Introduce el interés de la inversión:")
etiqueta_interes.place(x=10, y=70)

# Etiquetas para los errores
etiqueta_error_inversion = ttk.Label(text="")
etiqueta_error_inversion.place(x=300, y=10)
etiqueta_error_anios = ttk.Label(text="")
etiqueta_error_anios.place(x=300, y=40)
etiqueta_error_interes = ttk.Label(text="")
etiqueta_error_interes.place(x=300, y=70)

input_inversion = ttk.Entry()
input_inversion.place(x=200, y=10, width=80)
input_anios = ttk.Entry()
input_anios.place(x=200, y=40, width=80)
input_interes = ttk.Entry()
input_interes.place(x=200, y=70, width=80)

boton_calcular = ttk.Button(text="Calcular", command=calcularInversion)
boton_calcular.place(x=100, y=100)

etiqueta_monto = ttk.Label(text="El monto acumulado es:")
etiqueta_monto.place(x=10, y=130)
ventana.mainloop()
