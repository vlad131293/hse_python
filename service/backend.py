import requests


class WorkDays:

    def __init__(self) -> None:
        self.session = requests.Session()
        self.cash = []

    def validate_data(self, data: dict) -> None:
        
        pass

    
    def transorm_data(self, s: str) -> int:
        if isinstance(s, bytes):
            s = s.decode()
        
        temp = [int(x) for x in list(s)]
        num_days = len(temp) # Всего дней в месяце
        num_nwork_days = sum(temp) # Всего не рабочих дней 
        num_work_days = num_days - num_nwork_days # Всего рабочих

        return num_work_days

    def get_data(self, year: str, month: str) -> int:
        query = f"https://isdayoff.ru/api/getdata?year={year}&month={month}"

        result = self.session.get(query)
        content = result.content
        self.cash.append(content)
        
        num_work_days = self.transorm_data(content)

        return num_work_days

    def main(self, data: dict) -> dict:

        self.validate_data(data) # Валидация данных

        num_work_days = self.get_data(data['year'], data['month'])

        hour_income = data["salary"] / num_work_days
        hour_income = round(hour_income, 2)

        result = {
            **data,
            "hour_income": hour_income
        }
        return result
        

def main(year, month):
    model = WorkDays()
    n = model.get_data(year, month)
    return n


if __name__ == "__main__":
    n = main('2022', '5')
    print(n)