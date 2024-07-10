import tkinter as tk
from tkinter import messagebox

from opcion2 import evaluar_expresion


class InterfazCalculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora con Error")

        self.label = tk.Label(root, text="Ingrese la expresión:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Calcular", command=self.calcular)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calcular(self):
        expresion = self.entry.get()
        try:
            resultado = evaluar_expresion(expresion)
            self.result_label.config(text=f"Resultado: {resultado.valor} ± {format(resultado.error, '.10f')}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la expresión: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazCalculadora(root)
    root.mainloop()
