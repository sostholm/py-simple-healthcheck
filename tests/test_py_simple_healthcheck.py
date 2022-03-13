from py_simple_healthcheck import __version__, UnhealthyException, health_check, is_healthy

import os
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_health_check():
    health_check(20)

    with open('healthcheck') as file:
        timestamp, timeout = file.read().replace('\n', '').split(',')

    assert int(timestamp)
    assert int(timeout) == 20


def test_is_healthy():
    health_check(-20)

    with pytest.raises(UnhealthyException):
        is_healthy()