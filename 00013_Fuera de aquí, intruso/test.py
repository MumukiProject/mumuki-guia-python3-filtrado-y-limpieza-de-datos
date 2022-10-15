class Test(unittest.TestCase):

  def test_arboles_deberia_tener_ahora_menos_filas(self):
    self.assertTrue(len(muestra_arboles) == 9, "Debería haber menos árboles en el DataFrame original")