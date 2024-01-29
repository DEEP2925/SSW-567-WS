def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        triangle_type = "Isosceles"
    else: 
        triangle_type = "Scalene"

    if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
        triangle_type += " and Right Triangle"

    return triangle_type

if __name__ == "__main__":
    side1 = int(input("Please enter the 1st side of the triangle: "))
    side2 = int(input("Please enter the 2nd side of the triangle: "))
    side3 = int(input("Please enter the 3rd side of the triangle: "))

    result = classify_triangle(side1, side2, side3)
    print(result)