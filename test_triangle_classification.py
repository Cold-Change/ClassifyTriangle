"""Module providing classify triangle function and it's respective tests."""
import pytest

def classify_triangle(a, b, c):
    """Function dedicated to determining what typ of triangle three side lengths creates."""
    # Check that all sides are numbers
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "not a triangle"

    # Check for non-positive sides or all zeros
    if any(x < 0 for x in (a, b, c)) | (a == b == c == 0):
        return "not a triangle"

    # First test for Right Triangle
    if ((a**2 + b**2) == c**2) | ((c**2 + b**2) == a**2) | ((a**2 + c**2) == b**2):
        return "right"

    # Next test for Equilateral and Isosceles Triangles
    if (a == b) & (a == c):
        return "equilateral"
    if (a == b) | (a == c) | (b == c):
        return "isosceles"

    # Last, default to Scalene Triangle
    return "scalene"

class TestClassifyTriangle:
    """Class for testing triangles"""
    # -------------------------
    # Parametrized Tests
    # -------------------------
    @pytest.mark.parametrize("a,b,c", [
        (1, 2, 3),
        (3, 12, 7),
        (4, 5, 6),
        (7, 10, 12),
    ])
    def test_scalene(self, a, b, c):
        """Function testing scalene triangles."""
        assert classify_triangle(a, b, c) == "scalene"

    @pytest.mark.parametrize("a,b,c", [
        (1, 2, 2),
        (23, 14, 23),
        (5, 5, 8),
        (9, 12, 12),
    ])
    def test_isosceles(self, a, b, c):
        """Function testing isosceles triangles."""
        assert classify_triangle(a, b, c) == "isosceles"

    @pytest.mark.parametrize("a,b,c", [
        (3, 4, 5),
        (5, 3, 4),
        (10, 24, 26),
        (26, 10, 24),
        (8, 15, 17),
        (17, 8, 15),
        (9, 40, 41),
        (41, 9, 40),
    ])
    def test_right(self, a, b, c):
        """Function testing right triangles."""
        assert classify_triangle(a, b, c) == "right"

    @pytest.mark.parametrize("a,b,c", [
        (3, 3, 3),
        (54, 54, 54),
        (10, 10, 10),
        (100, 100, 100),
    ])
    def test_equilateral(self, a, b, c):
        """Function testing equilateral triangles."""
        assert classify_triangle(a, b, c) == "equilateral"

    @pytest.mark.parametrize("a,b,c", [
        ("b", "c", "a"),
        ("x", "y", 7),
        ("A", 12, "G"),
        ("f", 5, 7),
        (87, "c", "n"),
        (3, [1, 2], 87),
        (4, 5, None),
        (7, "z", "q"),
    ])
    def test_not_a_triangle(self, a, b, c):
        """Function testing non triangles."""
        assert classify_triangle(a, b, c) == "not a triangle"

    # -------------------------
    # Edge Cases
    # -------------------------
    def test_zero_sides(self):
        """Function testing all zeros triangles."""
        assert classify_triangle(0, 0, 0) == "not a triangle"

    def test_negative_sides(self):
        """Function testing negative non triangle."""
        assert classify_triangle(-3, -4, -5) == "not a triangle"

    def test_float_inputs(self):
        """Function testing double value triangles."""
        assert classify_triangle(3.0, 4.0, 5.0) == "right"
        assert classify_triangle(2.5, 2.5, 3.5) == "isosceles"

    def test_large_numbers(self):
        """Function testing large value triangle."""
        k = 10**6
        assert classify_triangle(3*k, 4*k, 5*k) == "right"

# End-of-file (EOF)
