"""
Script for Reservation - Booking Room.

Author: Kevin Cruz Mejia
"""

import json
import os


class Reservation:
    """Entity of a reservation."""

    def __init__(self, **kwargs):
        """Define a Reservation."""
        self.reservation_id = kwargs.get('reservation_id')
        self.customer_id = kwargs.get('customer_id')
        self.room_number = kwargs.get('room_number')
        self.start_date = kwargs.get('start_date')
        self.hotel_name = kwargs.get('hotel_name')
        self.end_date = kwargs.get('end_date')

    def save_to_file(self):
        """Save reservation into a file."""
        data = vars(self)
        filename = f"reservation_{self.reservation_id}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancel a reservation by removing its file."""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)

    @classmethod
    def create_reservation(cls, **kwargs):
        """Create a new reservation and saves it to a file."""
        reservation = cls(**kwargs)
        reservation.save_to_file()
        return reservation


def make_reservation(**kwargs):
    """Create a Reservation instance."""
    return Reservation(**kwargs)
