import tkinter as tk
from tkinter import messagebox
from CalculadoraConError import CalculadoraConError


class InterfazCalculadora:
    def __init__(self, root):
        self.calc = CalculadoraConError()
        self.root = root
        self.root.title("Calculadora con Error")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.entry_a = tk.Entry(self.frame, width=10)
        self.entry_a.grid(row=0, column=0, padx=5)
        self.entry_b = tk.Entry(self.frame, width=10)
        self.entry_b.grid(row=0, column=1, padx=5)

        self.resultado_label = tk.Label(self.frame, text="Resultado: ")
        self.resultado_label.grid(row=1, column=0, columnspan=2)
        self.error_label = tk.Label(self.frame, text="Error: ")
        self.error_label.grid(row=2, column=0, columnspan=2)

        self.boton_sumar = tk.Button(self.frame, text="Sumar", command=self.sumar)
        self.boton_sumar.grid(row=3, column=0, pady=5)
        self.boton_restar = tk.Button(self.frame, text="Restar", command=self.restar)
        self.boton_restar.grid(row=3, column=1, pady=5)
        self.boton_multiplicar = tk.Button(self.frame, text="Multiplicar", command=self.multiplicar)
        self.boton_multiplicar.grid(row=4, column=0, pady=5)
        self.boton_dividir = tk.Button(self.frame, text="Dividir", command=self.dividir)
        self.boton_dividir.grid(row=4, column=1, pady=5)

    def obtener_valores(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")
            return None, None

    def sumar(self):
        a, b = self.obtener_valores()
        if a is not None and b is not None:
            resultado, error = self.calc.sumar(a, b)
            self.actualizar_resultado(resultado, error)

    def restar(self):
        a, b = self.obtener_valores()
        if a is not None and b is not None:
            resultado, error = self.calc.restar(a, b)
            self.actualizar_resultado(resultado, error)

    def multiplicar(self):
        a, b = self.obtener_valores()
        if a is not None and b is not None:
            resultado, error = self.calc.multiplicar(a, b)
            self.actualizar_resultado(resultado, error)

    def dividir(self):
        a, b = self.obtener_valores()
        if a is not None and b is not None:
            try:
                resultado, error = self.calc.dividir(a, b)
                self.actualizar_resultado(resultado, error)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def actualizar_resultado(self, resultado, error):
        self.resultado_label.config(text=f"Resultado: {resultado}")
        self.error_label.config(text=f"Error: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazCalculadora(root)
    root.mainloop()
