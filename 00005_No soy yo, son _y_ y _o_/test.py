import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_solo_contiene_los_arboles_solicitados(self):
    self.assertEquals(len(self.resultado), 3)
    
  def test_solo_contiene_los_arboles_de_la_comuna_10(self):
    self.assertTrue(142527 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 142527")
    self.assertTrue(182465 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 182465")
    
  def test_solo_contiene_los_arboles_de_balvanera(self):
    self.assertTrue(8087 in list(self.resultado["tree_id"]), "Debería haber encontrado al árbol 8087")  
    