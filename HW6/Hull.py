#Giovanni Medrano
import sys, math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det(p, q, r):
    determinate = p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x

    return determinate
    pass


# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull(sorted_points):
    sorted_points.sort()
    coords = sorted_points
    length = len(coords)

    for i in range(length):
        x = coords[i][0]
        y = coords[i][1]
        coords[i] = Point(x, y)

    # Finding the bottom hull
    bottom_hull = []
    bottom_hull.append(coords[length - 1])
    bottom_hull.append(coords[length - 2])

    for j in range(length - 3, -1, -1):
        bottom_hull.append(coords[j])
        while (len(bottom_hull) >= 3):
            if det(bottom_hull[-1], bottom_hull[-2], bottom_hull[-3]) <= 0:
                del (bottom_hull[-2])
            else:
                break
    del bottom_hull[-1]
    del bottom_hull[0]

    # Finding the top hull
    x1 = coords[0]
    y1 = coords[1]
    top_hull = []
    top_hull.append(x1)
    top_hull.append(y1)
    for i in range(2, len(coords)):
        top_hull.append(coords[i])
        while len(top_hull) >= 3:
            if det(top_hull[-1], top_hull[-2], top_hull[-3]) <= 0:
                del top_hull[-2]
            else:
                break

    pass
    convex_hull1\
        = top_hull + bottom_hull

    return convex_hull1

    pass


# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly(convex_poly):
    final_point = (len(convex_poly) - 1)
    det = 0
    for obj in range(final_point):
        det += (convex_poly[obj + 1].y * convex_poly[obj].x) - (convex_poly[obj + 1].x * convex_poly[obj].y)
    final_det = (convex_poly[0].y * convex_poly[final_point].x) - (convex_poly[0].x * convex_poly[final_point].y)
    det = det + final_det
    area = abs(det) * (1 / 2)
    return area
    pass


def output(convex_hulls, area):
    print('Convex Hull')
    for i in range(len(convex_hulls)):
        print(convex_hulls[i])
    print()

    print('Area of Convex Hull =', area)


def main():
    # sorts the points by x axis only
    line = sys.stdin.readline()
    n = int(line)
    coordinates = []
    for i in range(n):
        coordinates.append(sys.stdin.readline().split())
    for x in range(len(coordinates)):
        for y in range(len(coordinates[x])):
            coordinates[x][y] = int(coordinates[x][y])
    convex_hulls = convex_hull(coordinates)
    area = area_poly(convex_hulls)
    output(convex_hulls, area)


pass

if __name__ == "__main__":
    main()
