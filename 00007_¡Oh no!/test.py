import pandas as pd

class Test(unittest.TestCase):
  def setUp(self):
    self.resultado = (
      #...content...#
    )  
  
  def test_genera_un_dataframe(self):
    self.assertEquals(type(self.resultado), pd.DataFrame)
    
  def test_no_contiene_fresnos(self):
    tree_ids = list(self.resultado["tree_id"])
 
    self.assertEquals(len(self.resultado), 5)
    self.assertEquals(142527 in tree_ids, "Debería haber encontrado al árbol 142527")
    self.assertEquals(24002305 in tree_ids, "Debería haber encontrado al árbol 24002305")
    self.assertEquals(2003708 in tree_ids, "Debería haber encontrado al árbol 2003708")
    self.assertEquals(13003665 in tree_ids, "Debería haber encontrado al árbol 13003665")    
 
