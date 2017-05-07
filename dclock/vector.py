class Vector:

    __slots__ = ('_vector', )

    def __init__(self) -> None:
        pass

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, str(self._vector))
