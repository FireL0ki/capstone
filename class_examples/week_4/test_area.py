from unittest import TestCase
import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        # A triangle with a height of 4 and a base of 5 should have area 10
        self.assertEqual(10, area.triangle_area(4, 5)) #expected outcome first, then run the function with the parameters and compare

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))  # use assertAlmostEqual to help prevent rounding errors caused by floating point math in computers

    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-3, 0)

        with self.assertRaises(ValueError):
            area.triangle_area(-3, -3)        
            
        with self.assertRaises(ValueError):
            area.triangle_area(0, -3)

    def test_base_height_zero(self):
        self.assertEqual(0, area.triangle_area(0, 10))
        self.assertEqual(0, area.triangle_area(10, 0))
        self.assertEqual(0, area.triangle_area(0, 0))