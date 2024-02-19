"""Script fot customer data."""

import json
import os


class Customer:
    """Entity of a customer."""

    def __init__(self, customer_id, name, email):
        """Define a Customer object with attributes."""
        if isinstance(name, int):
            raise ValueError("El nombre debe tener letras")
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.filename = f"customer_{customer_id}.json"

    def save_to_file(self):
        """Save customer data to a file."""
        data = {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def create_customer(customer_id, name, email):
        """Create a new customer and saves it to a file."""
        customer = Customer(customer_id, name, email)
        customer.save_to_file()
        return customer

    @staticmethod
    def delete_customer(customer_id):
        """Delete a customer's data file."""
        filename = f"customer_{customer_id}.json"
        os.remove(filename)

    def display_customer_info(self):
        """Display the customer's information."""
        print(f"""Customer ID: {self.customer_id},
              Name: {self.name}, Email: {self.email}""")

    def update_details(self, name=None, email=None):
        """Update customer details and saves to file."""
        if name:
            self.name = name
        if email:
            self.email = email
        self.save_to_file()

    @staticmethod
    def load_customer(customer_id):
        """Load a customer's data from a file."""
        filename = f"customer_{customer_id}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Customer(data['customer_id'], data['name'], data['email'])
