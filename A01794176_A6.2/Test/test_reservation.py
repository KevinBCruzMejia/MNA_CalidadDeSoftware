"""Unit tests for the Reservation class."""

import unittest
import coverage
import os
import sys
sys.path.append("C:\\Users\\Professional\\NoteBook\\ITESM\\Calidad de software\\Ejercicio de programacion 3\\Scripts")
from reservation import Reservation, make_reservation


class TestReservation(unittest.TestCase):
    """Testings for functionality of the Reservation class."""
    def setUp(self):
        """Create a reservation instance before each test."""
        self.reservation_data = {
            'reservation_id': 123,
            'customer_id': 1,
            'hotel_name': 'Hotel California',
            'room_number': 101,
            'start_date': '2024-02-01',
            'end_date': '2024-02-05'
        }
        self.reservation = make_reservation(**self.reservation_data)

    def test_reservation_initialization(self):
        """Testing for the initialization of a reservation."""
        for key, value in self.reservation_data.items():
            self.assertEqual(getattr(self.reservation, key), value)

    def test_save_to_file(self):
        """Testing for saving a reservation."""
        self.reservation.save_to_file()
        expected_filename = f"reservation_{self.reservation.reservation_id}.json"
        self.assertTrue(os.path.exists(expected_filename))
        os.remove(expected_filename)

    def test_cancel_reservation(self):
        """Testing for canceling a reservation by removing its file."""
        self.reservation.save_to_file()
        Reservation.cancel_reservation(self.reservation.reservation_id)
        expected_filename = f"reservation_{self.reservation.reservation_id}.json"
        self.assertFalse(os.path.exists(expected_filename))



if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  # catch-all except clause
        pass

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")