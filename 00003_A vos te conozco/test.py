import pandas as pd

class Test(unittest.TestCase):
  def test_genera_un_dataframe(self):
    self.assertEquals(type(sauces), pd.DataFrame)
    
  def test_sauces_solo_contiene_sauces(self):
    self.assertEquals(len(sauces), 1)