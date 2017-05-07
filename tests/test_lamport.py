import pytest
from dclock import Lamport


def test_basic():
    lclock = Lamport()
    assert lclock.time() == 0

    lclock.increment()
    assert lclock.time() == 1

    other = Lamport(10)
    lclock.witness(other)

    assert other.time() == 10
    assert lclock.time() == 11

    other2 = Lamport(5)
    lclock.witness(other2)
    assert lclock.time() == 12
    assert other2.time() == 5

    assert lclock.__repr__() == "Lamport('12')"


def test_errors():
    with pytest.raises(ValueError):
        Lamport(-1)
