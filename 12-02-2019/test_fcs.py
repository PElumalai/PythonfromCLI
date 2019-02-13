import unittest
import fcs

class TestFcs(unittest.TestCase):
    
    def test_one_word(self):
        text = 'vinay'
        result = fcs.fcs_text(text)
        self.assertEqual(result, 'Vinay')
        
    def test_multiple_words(self):
        text = 'akash cibi yashwant'
        result = fcs.fcs_text(text)
        self.assertEqual(result, 'Akash Cibi Yashwant')

if __name__ == '__main__':
    unittest.main()
    
