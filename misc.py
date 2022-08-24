import random
import string

url_login = 'https://discord.com/api/v9/auth/login'
url_register = 'https://discord.com/api/v9/auth/register'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36', 'Content-type': 'application/json'}


def get_random_num_key(num=8):
    a = string.ascii_letters + string.digits
    key = random.sample(a, num)
    keys = "".join(key)
    return keys
