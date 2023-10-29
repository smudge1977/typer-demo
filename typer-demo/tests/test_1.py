import pytest  # noqa

import typer_demo
from typer_demo.app import summer

class Test_framework:
    def test_version(self):
        # TODO: Should match the VERSION file
        assert typer_demo.__version__ == "0.0.1"

    def test_summer(self):
        print(summer(2, 4))
        assert summer(1, 4) == 5


def test_fail_example():
    pytest.skip(reason="Don't understand to point of the fail as it still makes a fail!")
    assert 1 == 3
    
    pytest.fail(reason="bar")
    
    # old
    # pytest.fail(msg="foo")
    # new
    
    


def test_skip_example():
    # old
    # pytest.skip(msg="foo")
    # new
    pytest.skip(reason="bar")


def test_exit_example():
    # old
    # pytest.exit(msg="foo")
    # new
    pytest.exit(reason="bar")
