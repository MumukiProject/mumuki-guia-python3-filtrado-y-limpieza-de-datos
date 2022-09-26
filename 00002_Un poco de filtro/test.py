import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )

  def test_genera_un_dataframe(self):
    self.assertEquals(type(resultado), pd.DataFrame)
    
  def test_devuelve_solo_los_arboles_de_palermo(self):
    self.assertEquals(len(resultado), 10)