def triangle(side1, side2, side3):

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("This triangle can exist.")
    else:
        print("This triangle cannot exist.")

triangle(3, 4, 5)
triangle(1, 1, 5)