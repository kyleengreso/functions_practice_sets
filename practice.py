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
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    s = (a + b + c) / 2
    area = ((s) * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

a= float(input("Please enter the side (a): "))
b= float(input("Please enter the side (b): "))
c= float(input("Please enter side (c): "))

area = computes_area(a,b,c)
print(area)

def leap_year(a):
    if a % 4 == 0 and a % 100 != 0 or (a % 100 == 0 and a % 400 == 0):
        return True
    else:
        return False

year = int(input("Please enter a year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
