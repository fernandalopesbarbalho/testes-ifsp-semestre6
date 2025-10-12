import unittest
import numeroromano as nr

class TestConversaoRomano(unittest.TestCase):

    def setUp(self):
        print('Iniciando teste:', self._testMethodName)

    def tearDown(self):
        print('Finalizando teste:', self._testMethodName)

    def test_converte_I(self):
        self.assertEqual(1, nr.converte('I'), "Erro na conversão de 'I'")

    def test_converte_V(self):
        self.assertEqual(5, nr.converte('V'), "Erro na conversão de 'V'")

    def test_converte_II(self):
        self.assertEqual(2, nr.converte('II'), "Erro na conversão de 'II'")

    def test_converte_XXII(self):
        self.assertEqual(22, nr.converte('XXII'), "Erro na conversão de 'XXII'")

    def test_converte_IX(self):
        self.assertEqual(9, nr.converte('IX'), "Erro na conversão de 'IX'")

    def test_converte_XXIV(self):
        self.assertEqual(24, nr.converte('XXIV'), "Erro na conversão de 'XXIV'")

if __name__ == "__main__":
    unittest.main()