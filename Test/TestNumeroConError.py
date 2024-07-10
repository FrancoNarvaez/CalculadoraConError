import unittest
from CalculadoraConError import CalculadoraConError


class TestCalculadoraConError(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraConError()

    def test_sumar(self):
        resultado, error = self.calc.sumar(3.9, 2.1)
        self.assertEqual(resultado, 6.0)
        # El error debería ser 0.05 (para 3.9) + 0.05 (para 2.1) = 0.1
        self.assertAlmostEqual(error, 0.1)

    def test_sumar_2(self):
        resultado, error = self.calc.sumar(7, 3)
        self.assertEqual(resultado, 10)
        # El error debería ser 0.5 (para 7) + 0.5 (para 3) = 1.0
        self.assertEqual(error, 1.0)

    def test_restar(self):
        resultado, error = self.calc.restar(5, 3)
        self.assertEqual(resultado, 2)
        # El error debería ser 0.5 (para 5) + 0.5 (para 3) = 1.0
        self.assertAlmostEqual(error, 1.0)

    def test_multiplicar(self):
        resultado, error = self.calc.multiplicar(2.5, 4)
        self.assertEqual(resultado, 10.0)
        # El error relativo sería 0.05/2.5 (para 2.5) + 0.5/4.0 (para 4.0) = 0.02 + 0.0125 = 0.0325
        self.assertAlmostEqual(error, 10.0 * 0.145)

    def test_dividir(self):
        resultado, error = self.calc.dividir(7, 2)
        self.assertEqual(resultado, 3.5)
        # El error relativo sería 0.5/7.0 (para 7.0) + 0.5/2.0 (para 2.0) = 0.0714 + 0.25 = 0.3214
        self.assertAlmostEqual(error, 3.5 * 0.3214, places=3)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)


if __name__ == '__main__':
    unittest.main()
