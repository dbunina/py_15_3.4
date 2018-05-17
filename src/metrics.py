import requests

MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/counters'
STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'


class Counter:
    def __init__(self, token, counter_id):
        self.token = token
        self.counter_id = counter_id

    @property
    def users(self):
        return self.get_response('ym:s:users')

    @property
    def pageviews(self):
        return self.get_response('ym:s:pageviews')

    @property
    def visits(self):
        return self.get_response('ym:s:visits')

    def get_response(self, metrics):
        params = {
            'id': self.counter_id,
            'metrics': metrics,
            'oauth_token': self.token
        }
        response = requests.get(STAT_URL, params=params)
        return self._convert(response.json())

    @staticmethod
    def _convert(value):
        return ', '.join(str(int(x)) for x in value['totals'])


def get_counters(auth_token):
    response = requests.get(MANAGEMENT_URL, params={'oauth_token': auth_token})
    counters = response.json()['counters']
    return [c['id'] for c in counters]


def get_stats():
    auth_token = 'AQAAAAAMB4qoAAUBMuTxDt8AKEhJgcLvKq9d-20'

    for counter_id in get_counters(auth_token):
        print('Retrieving data for counter with id {}:'.format(counter_id))

        counter = Counter(auth_token, counter_id)
        print('Visits: {}'.format(counter.visits))
        print('Page views: {}'.format(counter.pageviews))
        print('Users: {}'.format(counter.users))

get_stats()
