import unittest
from app.api import *
from flask import current_app


class TestApiCalculation(unittest.TestCase):
    """Test case used to assess operations functions."""

    def test_add(self):
        self.assertEqual(add(x=39, y=3), 42)

    def test_product(self):
        self.assertEqual(multiply(x=6, y=7), 42)

    def test_divide(self):
        self.assertEqual(divide(x=84, y=2), 42)
        self.assertEqual(divide(x=10, y=0), "Can't divide by zero.")

    def test_substract(self):
        self.assertEqual(subtract(x=84, y=42), 42)


class TestFlaskApiExecution(unittest.TestCase):
    """Test case used to assess functionality of the application."""

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()