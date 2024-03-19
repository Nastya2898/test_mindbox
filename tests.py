import unittest
import area as figures


class TestFigures(unittest.TestCase):
    def test_area(self):
        area_data = {(6, ): 113.09733552923255, (6, 2, ): 12,(3, 4, 5, ): 6, }
        for keys, val in area_data.items():
            self.assertEqual(figures.area(*keys), val)

    def test_is_triangle(self):
        with self.assertRaises(ValueError): figures.area(1, 2, 3, )

    def test_is_right_triangle(self):
        data = { (3,4,5 ): True, (3,4,6 ): False,}
        for keys, val in data.items():
            self.assertEqual(figures.Triangle(*keys).right_triangle(), val)

if __name__ == '__main__':
    unittest.main()