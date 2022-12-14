from manual_csv_to_json import ManualConverter


class CsvConverter():

    def __init__(self, csv_file_name: str, json_file_name: str) -> None:
        self.csv_file_name = csv_file_name
        self.json_file_name = json_file_name

    def read_data_to_list(self) -> list:
        with open(self.csv_file_name, 'r') as file:
            content = file.readlines()
        return content

    def write_data(self, data: str) -> None:
        with open(self.json_file_name, 'w') as file:
            file.write(data)

    def convert(self) -> None:
        data = self.read_data_to_list()
        inner_converter = ManualConverter(data)
        json_ = inner_converter.get_json()

        self.write_data(json_)


def main(csv_file_name: str, json_file_name: str) -> None:
    converter = CsvConverter(csv_file_name, json_file_name)
    converter.convert()


if __name__ == "__main__":
    main('../data/input.csv', '../data/output.json')
