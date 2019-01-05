import unittest
import os

def analyze_text(filename):
    line = 0
    char = 0
    with open(filename, "rt", encoding = "utf-8") as f:
        for lines in f:
            line += 1
            char += len(lines)

        return line, char 

class TextAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename = "text_analyzer_test_file.txt"
        with open(self.filename, "wt", encoding = "utf-8") as f:
            f.writelines(["We don't need your civil war, \n",
            "it feeds the rich and buries the poor, \n",
            "We don't want your civil war, \n",
            "No No No"])

    def tearDown(self):
        try:
            os.remove(self.filename)        
        except:
            pass
    
    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 4)    

    def test_char_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 110)    

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text("nosuchfile")    

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))        


if __name__ == "__main__":
    unittest.main()        