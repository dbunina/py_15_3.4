from urllib.parse import urlencode

APP_ID = '7ab9dba3eb6d4fcc85e8e919a491bd40'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

AUTH_DATA = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))

AUTH_TOKEN = 'AQAAAAAMB4qoAAUBMuTxDt8AKEhJgcLvKq9d-20'
