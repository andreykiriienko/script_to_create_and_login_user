import requests
import json
from misc import headers, url_login, url_register, get_random_num_key

# Этап регистрации дискорда
email = input('Email: ')
login = input('Login: ')

payload_register = {"fingerprint": "1011958883746586704.qwk6a4ozdJFl95weABLn0mnNtEA", "email": email,
                    "username": login, "password": get_random_num_key(), "invite": None, "consent": True,
                    "date_of_birth": "2000-03-02", "gift_code_sku_id": None, "captcha_key": None,
                    "promotional_email_opt_in": True}

session = requests.Session()

response_register = session.post(url_register, data=json.dumps(payload_register), headers=headers)
# TODO - На данном этапе не нашел решения обойти капчу. Получаю правильный ответ от сервера.
## На данный момент работает только логин.

# =======================================================
# Этап логина в Дискорд
# Использовать для теста логина такие данные:
# логин - posogol498@gmail.com
# пароль - Dofemu377!

login = input('Login: ')
password = input('Password: ')

payload_login = {"login": login, "password": password, "undelete": False}

session = requests.Session()

response_login = session.post(url_login, data=json.dumps(payload_login), headers=headers)

data = json.loads(response_login.text)
print(data['token'])
