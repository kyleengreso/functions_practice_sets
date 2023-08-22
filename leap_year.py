def leap_year(a) -> bool:
    """
    Check if a given year is a leap year.

    Args:
        a (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if a % 4 == 0 and a % 100 != 0 or (a % 100 == 0 and a % 400 == 0):
        return True
    else:
        return False

year = int(input("Please enter a year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")