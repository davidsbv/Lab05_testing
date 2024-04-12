# test_basicMathOps.py

# Librería para pruebas unitarias
import unittest
from basicMathOps import sumar

# Clase que recibe una prueba unitaria como parámetro
class TestSumar(unittest.TestCase):

    # Método para probar suma
    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(1, -1), -0)
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()