import math

def area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.
    Returns the area rounded to 2 decimal places, or an error message if radius <= 0.
    """
    if radius <= 0:
        return "Radius must be greater than 0"
    area = math.pi * radius ** 2
    return round(area, 2)

# Example usage (you can comment this out or keep it for testing)
if __name__ == "__main__":
    r = float(input("Enter radius: "))
    print("Area:", area_of_circle(r))