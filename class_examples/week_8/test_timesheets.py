import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimeSheet(TestCase):

    """ mock input()  and force it to return a value """

    # creates a mock that returns the value '2' -- these are values to be tested
    @patch('builtins.input', side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)


    @patch('builtins.input', side_effect=['bird', 'cat', 'horse789', '2'])
    def test_get_hours_reject_non_numbers(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)


    @patch('builtins.input', side_effect=['-2', '78', '-555', '10'])
    def test_get_hours_for_day_greater_than_zero(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(10, hours)


    @patch('builtins.input', side_effect=['99', '24.23', '5'])
    def test_get_hours_for_day_less_than_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(5, hours)


    @patch('builtins.print')
    def test_display_total(self, mock_print):
        timesheets.display_total(246)
        mock_print.assert_called_once_with('Total hours worked: 246')

    
    @patch('timesheets.alert')
    def test_alert_not_meeting_min_hours_does_not_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)
        mock_alert.assert_called_once()


    @patch('timesheets.alert')
    def test_alert_not_meeting_min_hours_does_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(40, 30)
        mock_alert.assert_not_called()


    @patch('timesheets.get_hours_for_day', side_effects=[5, 7, 9])
    def test_get_hours(self, mock_get_hours):
        # mock_hours = [5, 7, 9]
        # mock_get_hours.side_effects = mock_hours
        days = ['m', 't', 'w']
        expected_hours = dict(zip(days,[5, 7, 9]))  # creates a dictionary { 'm': 5, 't': 7 ... }
        hours = timesheets.get_hours(days)
        self.assertEqual(expected_hours, hours)

    
    @patch('builtins.print')
    def test_display_hours(self, mock_print):

        # arrange
        example = {'M': 3, 'T': 12, 'W': 8.50}
        expected_table_calls = {
            call('Day                     Hours Worked            '),
            call('M                       3                       '),
            call('M                       12                      '),
            call('M                       8.5                     '),
        }

        # action
        timesheets.display_hours(example)
        # assert
        mock_print.assert_has_calls(expected_table_calls)


    def test_total_hours(self):
        example = {'M': 3, 'T': 12, 'W': 8.50}
        total = timesheets.total_hours(example)
        expected_total = 3 + 12 + 8.5
        self.assertEqual(total, expected_total)


# to run test via python interpreter
if __name__ == '__main__':
    unittest.main()
