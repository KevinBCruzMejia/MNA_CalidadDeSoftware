"""Unit tests for the Hotel class."""

import unittest
import coverage
import os
import sys
sys.path.append("C:\\Users\\Professional\\NoteBook\\ITESM\\Calidad de software\\Ejercicio de programacion 3\\Scripts")
from hotel import Hotel
from room import Room


class TestHotel(unittest.TestCase):
    """Testing use cases for the Hotel class."""
    
    def setUp(self):
        self.hotel = Hotel("Test Hotel", "Test Location")
        test_room = Room(room_number=101, room_type="single", price=400.00, is_available=True)
        self.hotel.rooms.append(test_room)

    def test_create_hotel(self):
        """Testing for creating a hotel correctly initializes its attributes."""
        name = "My Hotel"
        location = "Mexico City"
        hotel = Hotel.create_hotel(name, location)
        self.assertEqual(hotel.name, name, "Nombre de hotel debe corresponder al proveido.")
        self.assertEqual(hotel.location, location, "Localizacion de hotel debe corresponder al proveido.")
        os.remove(hotel.filename)

    def test_delete_hotel(self):
        """Testing for deleting a hotel."""
        hotel = Hotel.create_hotel("Hotel de prueba", "Localizacion de prueba")
        self.assertTrue(os.path.exists(hotel.filename), "Datos de archivo del Hotel deben existir antes del borrado.")
        Hotel.delete_hotel(hotel)
        self.assertFalse(os.path.exists(hotel.filename), "Datos delk Hotel deben ser borrados.")

    def test_display_information(self):
        """Testing for  displaying hotel information"""
        expected_output = "Hotel Name: Test Hotel, Location: Test Location"
        self.assertEqual(self.hotel.display_information(), expected_output)

    def test_modify_information(self):
        """Testing for hotel information."""
        new_name = "Actualizado Test Hotel"
        new_location = "Actualizado Test Location"
        self.hotel.modify_information(new_name=new_name, new_location=new_location)

        # Verify that the hotel's information has been updated
        self.assertEqual(self.hotel.name, new_name, "Nombre del Hotel seria actualizado.")
        self.assertEqual(self.hotel.location, new_location, "Localizacion del Hotel seria actualizado.")

    def test_reserve_room(self):
        """Testing for reserving a room."""

        room_number = 101

        result = self.hotel.reserve_room("reservation_id", "customer_id", room_number, "2024-02-01", "2024-02-05")

        self.assertTrue(result, "Reservacion de cuarto deberia tener exito.")
        reserved_room = next((r for r in self.hotel.rooms if r.room_number == room_number), None)
        self.assertIsNotNone(reserved_room, "Cuarto reservado deberia existir en el hotel.")
        self.assertFalse(reserved_room.is_available, "Cuarto deberia de cambiar su estado como no disponible despues de la reservacion.")

    def test_cancel_reservation(self):
        """Testing for canceling a reservation"""

        hotel = Hotel("Hotel para reservacion", "Localizacion para reservacion")
        room_number = 101
        hotel.rooms.append(Room(room_number, "double", 450))
        reservation_id = "reserv101"
        hotel.reserve_room(reservation_id, "customer101", room_number, "2024-02-01", "2024-02-05")


        hotel.cancel_reservation(reservation_id)


        room = next((room for room in hotel.rooms if room.room_number == room_number), None)
        self.assertIsNotNone(room, "El cuarto deberia de existir.")
        self.assertTrue(room.is_available, "El cuarto deberia estar disponible despues de cancelar la reservacion.")


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