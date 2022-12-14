import unittest
from manual_csv_to_json import ManualConverter


class TestManualCsvConverter(unittest.TestCase):

    def test_prepare_title_1(self):
        test = ManualConverter(['id,city', '1,Novgorod'])
        self.assertEqual(test.prepare_title(), ['id', 'city'])

    def test_prepare_title_2(self):
        test = ManualConverter(['id,city,country', '1,Novgorod,Russia'])
        self.assertEqual(test.prepare_title(), ['id', 'city', 'country'])

    def test_prepare_title_3(self):
        test = ManualConverter(['id', ''])
        self.assertEqual(test.prepare_title(), ['id'])

    def test_get_json_1(self):
        test = ManualConverter(['id', '1'])
        self.assertEqual(test.get_json(), '[{ "id": "1" }]')

    def test_get_json_2(self):
        test = ManualConverter(['id,city', '1,', '5,Novgorod'])
        self.assertEqual(test.get_json(), '[{ "id": "1", "city": "" }, { "id": "5", "city": "Novgorod" }]')

    def test_get_json_3(self):
        test = ManualConverter(['id,city,country', ',,'])
        self.assertEqual(test.get_json(), '[{ "id": "", "city": "", "country": "" }]')


if __name__ == "__main__":
    unittest.main()
