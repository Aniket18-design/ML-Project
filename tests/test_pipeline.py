import unittest
from scripts.run_pipeline import main

class TestPipeline(unittest.TestCase):
    
    def test_pipeline_runs(self):
        try:
            main()
            self.assertTrue(True)
        except Exception:
            self.fail("Pipeline execution failed")

if __name__ == "__main__":
    unittest.main()
