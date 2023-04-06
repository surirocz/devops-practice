import datetime
import unittest
from unittest.mock import Mock

sunday = datetime.datetime(year=2023, month=4, day=2)
monday = datetime.datetime(year=2023, month=4, day=3)

datetime = Mock()

class ProcessData:
    def add_two_integers(self, a, b):
        """Function to get sum of two integers"""
        return a + b


    def substract_two_integers(self, a, b):
        """A function to get the difference of two integers """
        return a - b

    def is_a_weekend(self):
        """Flag to check if the day is a weekend."""
        today = datetime.datetime.today()
        if today.weekday() == 5 or today.weekday() == 6:
            return True
        return False
    


class TestForProcessData(unittest.TestCase):
    def setUp(self):
        self.process_data =  ProcessData()

    def test_add_two_integers(self):
        result = self.process_data.add_two_integers(2, 3)
        assert 5 == result

    def test_substract_two_integers(self):
        result = self.process_data.substract_two_integers(100, 40)
        assert 60 == result
    
    def test_is_a_weekend_true(self):
        # Sunday
        datetime.datetime.today.return_value = sunday
        result = self.process_data.is_a_weekend()
        assert result is True
    
    def test_is_a_weekend_false(self):
        # Monday
        datetime.datetime.today.return_value = monday
        assert self.process_data.is_a_weekend() is False


unittest.main()