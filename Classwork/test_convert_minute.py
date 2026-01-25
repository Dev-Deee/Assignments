import unittest
import function_snacks

class TestConvertMinuteFunction(unittest.TestCase):
    def test_that_convert_minute_function_exist(self):
        function_snacks.convert_minutes(10)

    def test_that_convert_minute_function_returns_hours_and_minutes(self):
        actual = function_snacks.convert_minutes(130)
        expected = "2 hours 10 minutes"
        self.assertEqual(actual, expected)

