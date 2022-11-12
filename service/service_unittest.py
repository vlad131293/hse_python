import unittest

from backend import WorkDays


class TestWorkDays(unittest.TestCase):
    
    def setUp(self) -> None:
        self.model = WorkDays()

    def test_get_wd(self) -> None:
        n = self.model.get_wd(2022, 2)
        self.assertEqual(n, 19)
    
    def test_main(self) -> None:
        result = self.model.main({"year": 2023, "month": 1, "salary": 120000})
        self.assertDictEqual(result, {'year': 2023, 'month': 1, 'salary': 120000.0, 'hour_income': 882.35})


if __name__ == "__main__":
    unittest.main()
