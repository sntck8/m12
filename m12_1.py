import requests

r = requests.get('https://urban-university.pro/student/', auth=('user', 'pass'))
print("Код состояния: ", r.status_code)
print("Тип контента: ", r.headers['content-type'])
print("Соединение: ", r.headers['connection'])
print("Кодировка: ", r.encoding)
print("Контент в юникоде: ", r.text)
print("Состояние ответа: ", r.ok)