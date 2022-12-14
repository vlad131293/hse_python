import unittest
from backend import WorkDays


class TestWorkDays(unittest.TestCase):

    def setUp(self) -> None:
        self.model = WorkDays()

    def test_get_wd_1(self) -> None:
        n = self.model.get_wd(2022, 2)
        self.assertEqual(n, 19)

    def test_transorm_data_1(self) -> None:
        result = self.model.transform_data('0010101')
        self.assertEqual(result, 4)

    def test_transorm_data_2(self) -> None:
        result = self.model.transform_data(b'0010101110')
        self.assertEqual(result, 5)

    def test_main(self) -> None:
        result = self.model.main({"year": 2023, "month": 1, "salary": 120000})
        self.assertDictEqual(result, {
            'year': 2023, 'month': 1,
            'salary': 120000.0, 'hour_income': 882.35
            })


if __name__ == "__main__":
    unittest.main()
