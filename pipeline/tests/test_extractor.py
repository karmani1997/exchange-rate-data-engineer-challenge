import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
from etl.extractor import fetch_exchange_rates
from etl.config import API_KEY

class TestFetchExchangeRates(unittest.TestCase):

    @patch('etl.extractor.requests.get')
    def test_fetch_exchange_rates(self, mock_requests_get):
        # Define test parameters
        base_currency = 'USD'
        target_currencies = ['EUR', 'GBP']
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 3)
        expected_dates = ['2022-01-01', '2022-01-02', '2022-01-03']

        # Define mock response data
        mock_response = MagicMock()
        mock_response.json.return_value = {'date': '2022-01-01', 'base': 'USD', 'rates': {'EUR': 0.82, 'GBP': 0.73}}
        mock_requests_get.return_value = mock_response

        # Call the function
        result = fetch_exchange_rates(API_KEY, base_currency, target_currencies, start_date, end_date)

        # Assertions
        self.assertEqual(len(result), 3)  # Check if data fetched for each day
        for idx, item in enumerate(result):
            self.assertEqual(item['date'], expected_dates[idx])  # Check if date is correct
            self.assertIn('USD', item['base'])  # Check if base currency is correct
            for currency in target_currencies:
                self.assertIn(currency, item['rates'])  # Check if rates for target currencies are present
            break
if __name__ == '__main__':
    unittest.main()
