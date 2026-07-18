def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c
    
def equilateral(sides):
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if (not is_triangle(sides)):
        return False
    if (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]):
        return True
    else:
        return False

def scalene(sides):
    if (is_triangle(sides) and not isosceles(sides)):
        return True
    else:
        return False
