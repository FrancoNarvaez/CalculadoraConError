import math


class CalculadoraConError:
    def __init__(self):
        self.resultado = 0
        self.error = 0

    def calcular_cota_error(self, valor):
        if valor == 0:
            return 0
        if isinstance(valor, int) or valor.is_integer():
            cota_error = 0.5
        else:
            partes = str(valor).split('.')
            cifras_decimales = len(partes[1]) if len(partes) == 2 else 0
            cota_error = 0.5 * 10**(-cifras_decimales)
        return cota_error

    def sumar(self, a, b):
        cota_error_a = self.calcular_cota_error(a)
        cota_error_b = self.calcular_cota_error(b)
        self.resultado = a + b
        self.error = cota_error_a + cota_error_b
        return self.resultado, self.error

    def restar(self, a, b):
        cota_error_a = self.calcular_cota_error(a)
        cota_error_b = self.calcular_cota_error(b)
        self.resultado = a - b
        self.error = cota_error_a + cota_error_b
        return self.resultado, self.error

    def multiplicar(self, a, b):
        cota_error_a = self.calcular_cota_error(a)
        cota_error_b = self.calcular_cota_error(b)
        self.resultado = a * b
        self.error = ((cota_error_a / abs(a)) + (cota_error_b / abs(b))) * abs(self.resultado)
        return self.resultado, self.error

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por 0")
        cota_error_a = self.calcular_cota_error(a)
        cota_error_b = self.calcular_cota_error(b)
        self.resultado = a / b
        self.error = abs(self.resultado) * ((cota_error_a / abs(a)) + (cota_error_b / abs(b)))
        return self.resultado, self.error
