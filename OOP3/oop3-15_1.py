import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner  

class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius  

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    return (point_in_circle(circle, p1) and
            point_in_circle(circle, p2) and
            point_in_circle(circle, p3) and
            point_in_circle(circle, p4))
def rect_circle_overlap(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    return (point_in_circle(circle, p1) or
            point_in_circle(circle, p2) or
            point_in_circle(circle, p3) or
            point_in_circle(circle, p4))
center = Point(150, 100)
circle = Circle(center, 75)
p = Point(160, 110)
print("Point in circle:", point_in_circle(circle, p))
rect = Rectangle(50, 40, Point(130, 80))

print("Rectangle in circle:", rect_in_circle(circle, rect))
print("Rectangle overlap circle:", rect_circle_overlap(circle, rect))