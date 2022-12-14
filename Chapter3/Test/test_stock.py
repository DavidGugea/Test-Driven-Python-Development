import unittest
from datetime import datetime
from Chapter3.stock import Stock


class StockTest(unittest.TestCase):
    def setUp(self) -> None:
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """
        An update should set the price of the stock object
        We will be using the `datetime` module for the timestamp
        """
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        self.assertRaises(ValueError, self.goog.update, datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 13), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)


class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        timestamps = [
            datetime(2014, 2, 11),
            datetime(2014, 2, 12),
            datetime(2014, 2, 13),
        ]

        prices = [8, 10, 12]

        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

        self.assertTrue(self.goog.is_increasing_trend())


if __name__ == '__main__':
    unittest.main()
