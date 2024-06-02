# Python functions

# Problem: X is calculated by the formula X = 2 * Y + 3 * Z + 4 * W
# Y and Z are the ares of circles with radius p,q and r respectively
# Calculate X

p = 1
q = 2
r = 3

area_of_circleP = 3.14 * p * p
area_of_circleQ = 3.14 * q * q
area_of_circleR = 3.14 * r * r

X = 2 * area_of_circleP + 3 * area_of_circleQ + 4 * area_of_circleR
print(X)


def circleArea(radius):
    area = (22 / 7) * (radius ** 2)
    return area
print(2 * circleArea(1) + 3 * circleArea(2) + 4 * circleArea(3))


def grade(marks):
    if marks>=75:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks>=55:
        grade = "C"
    elif marks>=35:
        grade="S"
    else:
        grade="W"
    return grade


def grade(marks):
    if marks>=75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks>=55:
        return "C"
    elif marks>=35:
        return "S"
    else:
        return "W"