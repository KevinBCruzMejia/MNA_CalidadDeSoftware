"""Unit tests for the Room class."""

import unittest
import coverage
import sys
sys.path.append("C:\\Users\\Professional\\NoteBook\\ITESM\\Calidad de software\\Ejercicio de programacion 3\\Scripts")
from room import Room


class TestRoom(unittest.TestCase):
    """Testings for functionality of the Room class."""
    def setUp(self):
        """Create a room instance before each test."""
        self.room = Room(room_number=101, room_type='single', price=400.00, is_available=True)

    def test_room_initialization(self):
        """Testing for the initialization of a room."""
        self.assertEqual(self.room.room_number, 101)
        self.assertEqual(self.room.room_type, 'single')
        self.assertEqual(self.room.price, 400.00)
        self.assertTrue(self.room.is_available)

    def test_make_reservation(self):
        """Testing for making a reservation."""
        self.room.make_reservation()
        self.assertFalse(self.room.is_available)

    def test_cancel_reservation(self):
        """Testing for canceling a reservation."""
        self.room.make_reservation()
        self.room.cancel_reservation()
        self.assertTrue(self.room.is_available)

    def test_update_price(self):
        """Testing for updating the room's price."""
        new_price = 780.00
        self.room.update_price(new_price)
        self.assertEqual(self.room.price, new_price)
            
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