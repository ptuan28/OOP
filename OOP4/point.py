class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def copy(self):
        return Point(self.__x, self.__y)