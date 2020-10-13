class Vector2D:
    """
    Predstavlja vektor sa x i y koordinatama
    """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def X(self):
        return self.__x

    @property
    def Y(self):
        return self.__y

    def update(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

