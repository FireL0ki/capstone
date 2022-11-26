import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitCoin(TestCase):

    @patch('bitcoin.exchange_rate_dollars')
    def test_dollars_to_bitcoin(self, mock_rates):
        mock_rate = 16484.0462
        example_api_response = {"rates":{"CAD": mock_rate},"base":"USD","date":"2020-10-02"}
        mock_rates.side_effect = [ example_api_response ]
        converted = bitcoin.convert_bitcoin_to_dollars(10, 16484.0462)
        expected = 164840.462
        self.assertEqual(expected, converted)