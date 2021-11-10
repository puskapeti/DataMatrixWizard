class Sector:
    """Class for defining sectors"""

    def __init__(self, x, y):
        self.__has_above = False
        self.__has_below = False
        self.__has_left = False
        self.__has_right = False

        self.__x = x
        self.__y = y

    def __str__(self):
        return f"x={self.__x}\ty={self.__y}"

    """ PROPERTIES --------------------------------------------------------------------------------------------------"""

    @property
    def alone(self):
        return not (self.__has_right or self.__has_left or self.__has_below or self.__has_above)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def above(self):
        return self.__has_above

    @above.setter
    def above(self, value):
        self.__has_above = value

    @property
    def below(self):
        return self.__has_below

    @below.setter
    def below(self, value):
        self.__has_below = value

    @property
    def left(self):
        return self.__has_left

    @left.setter
    def left(self, value):
        self.__has_left = value

    @property
    def right(self):
        return self.__has_right

    @right.setter
    def right(self, value):
        self.__has_right = value


if __name__ == '__main__':
    a = Sector(0, 0)
    b = Sector(10, 0)

    print(a + b)
