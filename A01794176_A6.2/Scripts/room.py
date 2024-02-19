"""
Script for defining and control the room entety.

Author: Kevin Cruz Mejia
Date: February 17, 2024
"""


class Room:
    """Entity of a room in a hotel."""

    def __init__(self, room_number, room_type, price, is_available=True):
        """Define a Room with price, type, number, and availability."""
        if isinstance(price, str):
            raise ValueError("El precio debe ser un entero")
        self.price = price
        if isinstance(room_type, int):
            raise ValueError("El room type debe tener letras")
        self.room_type = room_type
        if isinstance(room_number, str):
            raise ValueError("El numero debe ser un entero")
        self.room_number = room_number
        self.is_available = is_available

    def make_reservation(self):
        """Put the room as not available."""
        self.is_available = False

    def cancel_reservation(self):
        """Put the room as available."""
        self.is_available = True

    def update_price(self, new_price):
        """Update the room's price."""
        self.price = new_price

    @classmethod
    def from_dict(cls, data):
        """Create a Room instance from a dictionary."""
        return cls(
            room_number=data['room_number'],
            room_type=data['room_type'],
            price=data['price'],
            is_available=data.get('is_available', True)
        )

    def to_dict(self):
        """
        Convert into a dictionary making it easier to serialize.

        especially for saving the room data in format JSON.

        Returns a dictionary:
            A dictionary containing the room's properties.
        """
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price': self.price,
            'is_available': self.is_available
        }
