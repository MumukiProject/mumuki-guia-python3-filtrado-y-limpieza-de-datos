import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )  
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_no_contiene_fresnos(self):
    self.assertEquals(len(self.resultado), 5)
    
    self.assertEquals(4101876 in list(self.resultado.iloc["tree_id"]), "Debería haber encontrado al árbol 4101876")
    self.assertEquals(142527 in list(self.resultado.iloc["tree_id"]), "Debería haber encontrado al árbol 142527")
    self.assertEquals(24002305 in list(self.resultado.iloc["tree_id"]), "Debería haber encontrado al árbol 24002305")
    self.assertEquals(2003708 in list(self.resultado.iloc["tree_id"]), "Debería haber encontrado al árbol 2003708")
    self.assertEquals(13003665 in list(self.resultado.iloc["tree_id"]), "Debería haber encontrado al árbol 13003665")    
