import pandas as pd

class Test(unittest.TestCase):
  def test_genera_un_dataframe(self):
    self.assertEquals(type(meliaceas_comuna_10), pd.DataFrame)
    
  def test_sauces_solo_contiene_meliaceas_de_la_comuna_10(self):
    self.assertEquals(len(meliaceas_comuna_10), 1)
    self.assertEquals(meliaceas_comuna_10.iloc[0]["tree_id"], 13003665, "Debería haber encontrado al árbol 13003665")
    
    