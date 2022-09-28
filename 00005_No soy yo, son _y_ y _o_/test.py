import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_sauces_solo_contiene_sauces(self):
    self.assertEquals(len(self.resultado), 1)
    self.assertEquals(self.resultado.iloc[0]["tree_id"], 13003665, "Debería haber encontrado al árbol 13003665")
    