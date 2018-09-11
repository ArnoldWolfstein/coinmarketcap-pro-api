import contextlib
import unittest

from coinmarketcap import CoinMarketCap
from coinmarketcap.exceptions import *


@contextlib.contextmanager
def raises(exception):
    try:
        yield
    except exception as e:
        assert True
    else:
        assert False


class CoinMarketCapTestCase(unittest.TestCase):
    def test_api_key_missing(self):
        _client = CoinMarketCap(None, is_sandbox=True)

        with raises(UnauthorizedException):
            _client.fetch('/cryptocurrency/info', params={'symbol': 'BTC'})


if __name__ == '__main__':
    unittest.main()
