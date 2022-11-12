import unittest

from backend import WorkDays


class TestWorkDays(unittest.TestCase):
    
    def test_num_workdays(self):
        model = WorkDays()
        n = model.get_data('2022', '2')
        self.assertEquals(n, 19)

if __name__ == "__main__":
    unittest.main()