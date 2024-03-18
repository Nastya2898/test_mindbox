import unittest
import area as figures


class TestFigures(unittest.TestCase):
    def test_area(self):
        """проверка вычисления площадей"""
        area_data = {
            (4, ): 50.26548245743669,
            (4, 2, ): 8,
            (4, 5, 6, ): 9.921567416492215,
         }
        for keys, val in area_data.items():
            self.assertEqual(figures.area(*keys), val)

    def test_is_triangle(self):
        """треугольник ли?"""
        with self.assertRaises(ValueError):
            figures.area(1, 2, 3, )

    def test_is_right_triangle(self):
        """п/у треугольник ли?"""
        data = {
            (3, 4, 5, ): True,
            (145, 105, 100, ): True,
            (70, 130, 110, ): False,
        }
        for keys, val in data.items():
            self.assertEqual(figures.Triangle(*keys).right_triangle(), val)

if __name__ == '__main__':
    unittest.main()