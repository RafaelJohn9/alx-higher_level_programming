import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_area(self):
        self.assertEqual(self.square.area(), 25)

    def test_to_dictionary(self):
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_update(self):
        self.square.update(10, 20, 30, 40)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 30)
        self.assertEqual(self.square.y, 40)

        self.square.update(x=100, y=200)
        self.assertEqual(self.square.x, 100)
        self.assertEqual(self.square.y, 200)

    def test_constructor_valid_attributes(self):
        square = Square(10, 30, 40)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_constructor_invalid_size(self):
        with self.assertRaises(ValueError):
            Square(-5, 2, 3)

    def test_constructor_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("invalid", 2, 3)

    def test_constructor_invalid_x(self):
        with self.assertRaises(ValueError):
            Square(5, -2, 3)

    def test_constructor_invalid_y(self):
        with self.assertRaises(ValueError):
            Square(5, 2, -3)

    def test_constructor_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(5, "invalid", 3)

    def test_constructor_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(5, 2, "invalid")

    def test_setters(self):
        with self.assertRaises(ValueError):
            self.square.size = -5

        with self.assertRaises(ValueError):
            self.square.x = -2

        with self.assertRaises(ValueError):
            self.square.y = -3

    def test_str(self):
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected_str)
