import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(resultado), pd.DataFrame)
    
  def test_solo_contiene_oleaceas_de_la_comuna_10(self):
    self.assertEquals(len(resultado), 1)
    self.assertEquals(resultado.iloc[0]["tree_id"], 182465, "Debería haber encontrado al árbol 182465")
    
    