import pytest


@pytest.fixture(scope='function')
def check_cc():
    return 'test cryptochecker'

