import unittest
import pandas as pd
import warnings
from datetime import datetime
from etl.transformer import transform_data
warnings.filterwarnings("ignore")

class TestTransformData(unittest.TestCase):

    def test_transform_data(self):
        # Define sample input data
        exchange_rates = [
            {
                'success': True,
                'timestamp': 1705276799,
                'historical': False,
                'base': 'USD',
                'date': '2022-01-01',
                'rates': {'EUR': 0.82, 'GBP': 0.73}
            },
            {
                'success': True,
                'timestamp': 1705363199,
                'historical': False,
                'base': 'USD',
                'date': '2022-01-02',
                'rates': {'EUR': 0.83, 'GBP': 0.74}
            }
        ]

        # Define expected output DataFrame
        expected_df = pd.DataFrame({
            'timestamp': [pd.to_datetime(1705276799, unit='s'), pd.to_datetime(1705276799, unit='s'),
                          pd.to_datetime(1705363199, unit='s'), pd.to_datetime(1705363199, unit='s')],
            'base_currency': ['USD', 'USD', 'USD', 'USD'],
            'date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
            'target_currency_code': ['EUR', 'GBP', 'EUR', 'GBP'],
            'exchange_rate': [0.82, 0.73, 0.83, 0.74],
            'rate_id': [1, 2, 3, 4]
        })

        # Call the function
        result_df = transform_data(exchange_rates)

        # Assertions
        pd.testing.assert_frame_equal(result_df.sort_index(axis=1), expected_df.sort_index(axis=1))

if __name__ == '__main__':
    unittest.main()
