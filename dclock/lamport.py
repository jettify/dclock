
class Lamport:

    __slots__ = ('_counter', )

    def __init__(self, initial_clock: int = 0) -> None:
        if initial_clock < 0:
            raise ValueError("Initial clock value should be positive or 0")
        self._counter = initial_clock

    def time(self)-> int:
        return self._counter

    def increment(self) -> int:
        self._counter += 1
        return self._counter

    def witness(self, other: 'Lamport') -> 'Lamport':
        self._counter = max(other.time(), self._counter) + 1
        return self

    def __repr__(self):
        return "{}('{}')".format(self.__class__.__name__, str(self._counter))
