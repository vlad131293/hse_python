import unittest
from md_converter import Converter


class TestMdConverter(unittest.TestCase):

    data = "# title Hello!\n# date 2022\n# description hello world!"

    title = 'My title'
    description = 'hello world!'
    source_code = "print('2022')"
    md_data = ("# title Print Greeting\n# description print Greeting!\n"
               "# ---end----\n\nprint('Greeting!')\n")

    def setUp(self) -> None:
        self.model = Converter()

    def test_prepare_md_titles(self):
        result = self.model.prepare_md_titles(self.data)
        expected = ('Hello!', 'hello world!')
        self.assertTupleEqual(result, expected)

    def test_prepare_md_format(self):
        result = self.model.prepare_md_format(
            self.title, self.description, self.source_code
        )
        expected = ("+ [My title](#my-title)\n\n"
                    "## My title\n\n"
                    "hello world!\n\n"
                    "```python\n"
                    "print('2022')\n"
                    "```")
        self.assertEqual(result, expected)

    def test_convert_data(self):
        result = self.model.convert_data(self.md_data)
        expected = ("+ [Print Greeting](#print-greeting)\n\n"
                    "## Print Greeting\n\n"
                    "print Greeting!\n\n"
                    "```python\nprint('Greeting!')\n```")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
