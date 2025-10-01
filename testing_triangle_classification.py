def classify_triangle(a, b, c):
    # Preliminary test for whether the arguements create a valid triangle (are all values numbers)
    if (not isinstance(a, (int, float, complex))) | (not isinstance(b, (int, float, complex))) | (not isinstance(c, (int, float, complex))):
        return "not a triangle"

    # First test for Right Triangle
    if ((a**2 + b**2) == c**2) | ((c**2 + b**2) == a**2) | ((a**2 + c**2) == b**2):
        return "right"

    # Next test for Equilateral and Isosceles Triangles
    if (a == b) & (a == c):
        return "equilateral"
    elif (a == b) | (a == c) | (b == c):
        return "isosceles"
    
    # Last, default to Scalene Triangle
    return "scalene"

def test_classify_triangle():
    assert classify_triangle(1,2,3) == "scalene"
    assert classify_triangle(3,12,7) == "scalene"
    assert classify_triangle(1,2,2) == "isosceles"
    assert classify_triangle(23,14,23) == "isosceles"
    assert classify_triangle(3,4,5) == "right"
    assert classify_triangle(5,3,4) == "right"
    assert classify_triangle(10,24,26) == "right"
    assert classify_triangle(26,10,24) == "right"
    assert classify_triangle(3,3,3) == "equilateral"
    assert classify_triangle(54,54,54) == "equilateral"
    assert classify_triangle("A",12,5) == "not a triangle"
    assert classify_triangle(12,5,"A") == "not a triangle"
    assert classify_triangle("b","c","a") == "not a triangle"