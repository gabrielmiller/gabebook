import unittest
from helpers import Helpers

class HelpersTests(unittest.TestCase):
    def setUp(self):
        self.sut = Helpers()

    def test_parse_post_new_entries(self):
        input = "This is a test post with a [New Entry] inside of it."
        expectation = [{ 'firstName': 'New', 'lastName': 'Entry' }]

        output = self.sut.parse_post(input)
        self.assertEqual(output, expectation, "parse_post output mismatch")

    def test_parse_post_existing_entries(self):
        input = "This is a test post with an [17:Existing Entry] inside of it."
        expectation = [{ 'id': 17 }]

        output = self.sut.parse_post(input)
        self.assertEqual(output, expectation, "parse_post output mismatch")

    def test_parse_post_new_and_existing_entries(self):
        input = "This is a test post with both a [New Entry] and an [18:Existing Entry] inside of it."
        expectation = [{ 'firstName': 'New', 'lastName': 'Entry' }, { 'id': 18 }]

        output = self.sut.parse_post(input)
        self.assertEqual(output, expectation, "parse_post output mismatch")

if __name__ == "__main__":
    unittest.main()
