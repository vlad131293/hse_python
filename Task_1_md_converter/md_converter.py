INPUT_CODE_DELIMITER = '# ---end----'


class Converter:

    def __init__(self):
        pass

    def read_data(self):

        with open(self.in_file, 'r') as file:
            content = file.read()
        return content

    def write_data(self, data):

        with open(self.out_file, 'w') as file:
            # content = "\n".join(data)
            file.write(data)

    def prepare_md_titles(self, data):
        title = description = None

        for line in data.split('\n'):
            if line.startswith('# title'):
                title = line.replace('# title ', '')
            elif line.startswith('# description'):
                description = line.replace('# description ', '')

        return title, description

    def prepare_md_format(self, title, description, source_code):
        md_link = '-'.join(title.lower().split())

        template = (f'+ [{title}](#{md_link})\n\n'
                    f'## {title}\n\n'
                    f'{description}\n\n'
                    '```python\n'
                    f'{source_code.strip()}\n'
                    '```')
        return template

    def convert_data(self, data):
        titles, source_code = data.split(INPUT_CODE_DELIMITER)
        title, description = self.prepare_md_titles(titles)
        format = self.prepare_md_format(title, description, source_code)
        return format

    def main(self, in_file: str, out_file: str):
        self.in_file = in_file
        self.out_file = out_file
        content = self.read_data()
        format = self.convert_data(content)
        self.write_data(format)


def main():
    converter = Converter()
    converter.main(in_file='test.py', out_file='result.md')


if __name__ == "__main__":
    main()
