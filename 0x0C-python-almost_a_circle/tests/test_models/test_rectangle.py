import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_attributes(self):
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    def test_to_dictionary(self):
        expected_dict = {
            "x": 2,
            "y": 3,
            "id": 1,
            "width": 5,
            "height": 10
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_update(self):
        self.rectangle.update(10, 20, 30, 40, 50)
        self.assertEqual(self.rectangle.id, 10)
        self.assertEqual(self.rectangle.width, 20)
        self.assertEqual(self.rectangle.height, 30)
        self.assertEqual(self.rectangle.x, 40)
        self.assertEqual(self.rectangle.y, 50)

        self.rectangle.update(x=100, y=200)
        self.assertEqual(self.rectangle.x, 100)
        self.assertEqual(self.rectangle.y, 200)

    def test_constructor_valid_attributes(self):
        rectangle = Rectangle(10, 20, 30, 40)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 30)
        self.assertEqual(rectangle.y, 40)

    def test_constructor_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3)

    def test_constructor_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3)

    def test_constructor_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_constructor_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_constructor_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3)

    def test_constructor_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 2, 3)

    def test_constructor_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3)

    def test_constructor_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid")

    def test_setters(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

        with self.assertRaises(ValueError):
            self.rectangle.height = -10

        with self.assertRaises(ValueError):
            self.rectangle.x = -2

        with self.assertRaises(ValueError):
            self.rectangle.y = -3

    def test_str(self):
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_str)
