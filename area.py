def computes_area(a, b, c) -> float:
    """
    Computes the area of a triangle given the lengths of its sides.

    Parameters:
    - a: float, length of side a
    - b: float, length of side b
    - c: float, length of side c

    Returns:
    - float, area of the triangle
    """
    s = (a + b + c) / 2
    area = ((s) * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

a= float(input("Please enter the side (a): "))
b= float(input("Please enter the side (b): "))
c= float(input("Please enter side (c): "))

area = computes_area(a,b,c)
print(area)


