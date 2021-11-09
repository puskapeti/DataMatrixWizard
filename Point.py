
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"x={self.__x}\tx={self.__y}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


if __name__ == '__main__':
    a = Point(0, 0)
    b = Point(10, 0)

    print( a +b)
