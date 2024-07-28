import pytest

from dto.person import Person


@pytest.fixture
def person():
    return Person("nicolas", "montano", 1992, 1, 1)


def test_add_money(person):
    person.add_money(10)
    person.add_money(10)
    assert (person.money == 20)
