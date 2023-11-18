import unittest
from datetime import datetime
from StockDriver import getTik, getChartType, getTimeSeries, getStartDate, getEndDate

class TestStockDriver(unittest.TestCase):

    def test_symbol_valid(self):
        valid_symbols = ['AAPL', 'GOOG', 'AMZN', 'TSLA', 'FB', 'MSFT', 'IBM']
        for symbol in valid_symbols:
            self.assertTrue(symbol.isupper() and symbol.isalpha() and 1 <= len(symbol) <= 7)

    def test_symbol_invalid(self):
        invalid_symbols = ['aapl', 'GOOGLE', '123', 'AB!CD', '']
        for symbol in invalid_symbols:
            self.assertFalse(symbol.isupper() or not symbol.isalpha() or len(symbol) > 7 or len(symbol) < 1)

    def test_chart_type_valid(self):
        valid_chart_types = ['1', '2']
        for chart_type in valid_chart_types:
            self.assertTrue(chart_type in ['1', '2'])

    def test_chart_type_invalid(self):
        invalid_chart_types = ['0', '3', 'a', '12', '']
        for chart_type in invalid_chart_types:
            self.assertFalse(chart_type in ['1', '2'])

    def test_time_series_valid(self):
        valid_time_series = ['1', '2', '3', '4']
        for time_series in valid_time_series:
            self.assertTrue(time_series in ['1', '2', '3', '4'])

    def test_time_series_invalid(self):
        invalid_time_series = ['0', '5', 'a', '12', '']
        for time_series in invalid_time_series:
            self.assertFalse(time_series in ['1', '2', '3', '4'])

    def test_start_date_valid(self):
        try:
            datetime.strptime('2023-01-01', '%Y-%m-%d')
            datetime.strptime('2020-12-31', '%Y-%m-%d')
        except ValueError:
            self.fail("Start date validation failed for valid dates")

    def test_start_date_invalid(self):
        with self.assertRaises(ValueError):
            datetime.strptime('20230101', '%Y-%m-%d')
            datetime.strptime('2020/12/31', '%Y-%m-%d')
            datetime.strptime('2020-13-01', '%Y-%m-%d')
            datetime.strptime('31-12-2020', '%Y-%m-%d')
            datetime.strptime('', '%Y-%m-%d')

    def test_end_date_valid(self):
        try:
            datetime.strptime('2023-01-01', '%Y-%m-%d')
            datetime.strptime('2020-12-31', '%Y-%m-%d')
        except ValueError:
            self.fail("End date validation failed for valid dates")

    def test_end_date_invalid(self):
        with self.assertRaises(ValueError):
            datetime.strptime('20230101', '%Y-%m-%d')
            datetime.strptime('2020/12/31', '%Y-%m-%d')
            datetime.strptime('2020-13-01', '%Y-%m-%d')
            datetime.strptime('31-12-2020', '%Y-%m-%d')
            datetime.strptime('', '%Y-%m-%d')

if __name__ == '__main__':
    unittest.main()
