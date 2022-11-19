class ManualConverter:

    def __init__(self, csv_data: list) -> None:
        self.title = csv_data[0]
        self.values = csv_data[1:]

    def prepare_title(self) -> list:
        title = self.title.strip().split(',')
        return title

    def prepare_row_values(self) -> list:
        if len(self.values) > 0:
            values = [val.strip().split(',') for val in self.values]
        else:
            title = self.prepare_title()
            values = [['' for _ in title]]

        return values

    def convert_row_to_json(self, data: dict) -> str:

        values = ['"{}": "{}"'.format(k, v) for k, v in data.items()]
        formatted_values = ', '.join(values)

        formatted_line = f"{{ {formatted_values} }}"
        return formatted_line

    def check_data(self, title: list, row_values: list) -> None:
        for row in row_values:
            assert len(title) == len(row), "Len title error"

    def get_json(self) -> str:
        title = self.prepare_title()
        row_values = self.prepare_row_values()
        self.check_data(title, row_values)

        rows = [dict(zip(title, row)) for row in row_values]
        result = [self.convert_row_to_json(row) for row in rows]

        return "[{}]".format(", ".join(result))
