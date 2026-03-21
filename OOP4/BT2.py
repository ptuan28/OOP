from point import Point
import copy
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 2)
        elif len(args) == 2 and all(isinstance(arg, Point) for arg in args):
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4 and all(isinstance(arg, (int, float)) for arg in args):
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):
            self.__d1 = copy.deepcopy(args[0].getD1())
            self.__d2 = copy.deepcopy(args[0].getD2())
        else:
            raise ValueError("Invalid arguments for LineSegment constructor")
    def __str__(self):
        return "[(%d, %d), (%d, %d)]" % (self.__d1.x, self.__d1.y, self.__d2.x, self.__d2.y)
    def getD1(self):
        return self.__d1
    def getD2(self):
        return self.__d2
    def setD1(self, d1):
        if isinstance(d1, Point):
            self.__d1 = d1
    def setD2(self, d2):
        if isinstance(d2, Point):
            self.__d2 = d2
    def printSegment(self):
        print(f"D1({self.__d1.x}, {self.__d1.y})")
        print(f"D2({self.__d2.x}, {self.__d2.y})")



        

