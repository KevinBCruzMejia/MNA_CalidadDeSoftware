"""Unit tests for the Customer class."""

import unittest
import coverage
import os
import io
from unittest.mock import patch
import sys
sys.path.append("C:\\Users\\Professional\\NoteBook\\ITESM\\Calidad de software\\Ejercicio de programacion 3\\Scripts")
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Tests for functionality of the Customer class."""
    def setUp(self):
        """Creates a customer instance before each test."""
        self.customer = Customer(customer_id=1, name='Kevin Cruz', email='kevincruz@example.com')

    def test_customer_initialization(self):
        """Testing of how we can create a customer."""
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, 'Kevin Cruz')
        self.assertEqual(self.customer.email, 'kevincruz@example.com')

    def test_delete_customer(self):
        """Testinf for deleting a customer."""
        customer_id = "customer01"
        Customer.create_customer(customer_id, "Kevin", "kevincru@example.com")
        expected_filename = f"customer_{customer_id}.json"
        self.assertTrue(os.path.exists(expected_filename), "Informacion del cliente en archivo deberia existir despues de su creacion")
        Customer.delete_customer(customer_id)
        self.assertFalse(os.path.exists(expected_filename), "IOnformacion del cliente en archivo deberia borrarse")

    def test_display_customer_info(self):
        """Test displaying customer information prints the correct details."""
        customer = Customer("customer02", "Kevin Cruz", "kevs@example.com")
        expected_output = "Customer ID: customer02,\n              Name: Kevin Cruz, Email: kevs@example.com\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            customer.display_customer_info()
            self.assertEqual(fake_out.getvalue(), expected_output,
                             "La salida deberia esta relacionada a la informacion del cliente.")

    def test_update_details(self):
        """Testing updating customer's information."""
        new_name = 'Kevin Cruz'
        new_email = 'kevincruz@example.com'
        self.customer.update_details(name=new_name, email=new_email)
        self.assertEqual(self.customer.name, new_name)
        self.assertEqual(self.customer.email, new_email)

    def test_load_customer(self):
        """Testing for loading a customer retrieves the correct information."""
        customer_id = "customer03"
        original_customer = Customer.create_customer(customer_id, "Mohamad Jhonson", "mjghon@example.com")

        loaded_customer = Customer.load_customer(customer_id)

        self.assertEqual(loaded_customer.customer_id, original_customer.customer_id, "Cliente ID deberia estar relacionado.")
        self.assertEqual(loaded_customer.name, original_customer.name, "Cliente name deberia estar relacionado.")
        self.assertEqual(loaded_customer.email, original_customer.email, "Cliente mail deberia estar relacionado.")
        os.remove(f"customer_{customer_id}.json")


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