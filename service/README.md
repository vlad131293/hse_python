## Hourly-wage-rate

### Запуск сервиса:
```uvicorn app:app --reload --host 0.0.0.0 --port 8899```

Адрес сервиса:
`http://127.0.0.1:8899/accept_data`

Документация сервиса:
`http://127.0.0.1:8899/redoc`

### Пример:
```python
import requests
import json

session = requests.Session()
res = session.post(
    "http://127.0.0.1:8899/accept_data",
    json={
        "year": 2023,
        "month": 1,
        "salary": 120000
    }
)

answer = json.loads(res.content)
print(answer)

# {'year': 2023, 'month': 1, 'salary': 120000.0, 'hour_income': 882.35}
```
