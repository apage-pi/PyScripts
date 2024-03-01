from fractions import Fraction
while True:
    print("1) Slope from coordinates")
    print("2) Slope from distances")
    type = int(input("Select (1 or 2): "))

    def simplify_fraction(num, denom):
        fraction = Fraction(num, denom)
        return fraction.numerator, fraction.denominator

    if type == 1:
        print("Remember: Coordinates are like this: (x, y)")
        x1 = int(input("Enter first x coordinate: "))
        y1 = int(input("Enter first y coordinate: "))
        x2 = int(input("Enter second x coordinate: "))
        y2 = int(input("Enter second y coordinate: "))
        xDist = x1 - x2
        yDist = y1 - y2
        if yDist % xDist == 0:
            slope = yDist / xDist
            print("Slope: {}".format(slope))
        else:
            slope = simply_num, simply_denom = simplify_fraction(yDist, xDist)
            print(''' {}
-----
 {}'''.format(simply_num, simply_denom))
    else:
        xDist = int(input("Distance between X coordinate points: "))
        yDist = int(input("Distance between Y coordinate points: "))
        if yDist % xDist == 0:
            slope = yDist / xDist
            print("Slope: {}".format(slope))
        else:
            slope = simply_num, simply_denom = simplify_fraction(yDist, xDist)
            print(''' {}
-----
 {}'''.format(simply_num, simply_denom))

