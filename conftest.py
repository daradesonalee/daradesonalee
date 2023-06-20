import pytest

from libs.pet_libs import PetLibs
from libs.interface import Interface

@pytest.fixture
def libs():
    petlib=PetLibs()

    return petlib

@pytest.fixture
def apis():
    inter=Interface()
    return inter