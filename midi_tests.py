from flask_app import name_to_midi
import unittest


class TestMids(unittest.TestCase):

    def test_name_midi(self):
        self.assertEqual(name_to_midi('C𝄲6'), 84.5, "Should be 84.5")
        self.assertEqual(name_to_midi('D3'), 50, "Should be 50")

if __name__ == "__main__":
    unittest.main()
