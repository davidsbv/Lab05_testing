# test_basicMathOps.py

# Librería para pruebas unitarias
import unittest
from basicMathOps import *

# Clase que recibe una prueba unitaria como parámetro
class TestSumar(unittest.TestCase):

    # Función para probar suma con tres llamadas al método assertEqual
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(1, -1), 0)
        self.assertEqual(sumar(-1, -1), -2)

class TestResta(unittest.TestCase):

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-5, 3), -8)
        self.assertEqual(restar(5, -3), 8)
        self.assertEqual(restar(-5, -3), -2)

class TestMultiplicacion(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(-5, 3), -15)
        self.assertEqual(multiplicar(5, -3), -15)
        self.assertEqual(multiplicar(-5, -3), 15)

class TestDivision(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(15, 3), 5)
        self.assertEqual(dividir(15, -3), -5)
        self.assertEqual(dividir(-15, 3), -5)
        self.assertRaises(dividir(15,0),ZeroDivisionError)
            

if __name__ == '__main__':
    unittest.main()