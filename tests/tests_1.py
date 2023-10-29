import pytest  # noqa

import typer_demo


class Test_framework:
    def test_version(self):
        # TODO: Should match the VERSION file
        assert typer_demo.__version__ == "0.0.0"

    def test_summer(self):
        assert typer_demo.app.summer(1, 4) == 5


def test_fail_example():
    # old
    # pytest.fail(msg="foo")
    # new
    pytest.fail(reason="bar")


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
