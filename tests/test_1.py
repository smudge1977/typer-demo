import importlib.metadata
from pathlib import Path

import pytest  # noqa

import typer_demo
from typer_demo.app import summer


def get_pyproject_version():
    root_dir = Path(__file__).parent.parent
    with open(f"{root_dir}/pyproject.toml", encoding="utf-8") as pyproject_toml:
        version = (
            next(line for line in pyproject_toml if line.startswith("version"))
            .split("=")[1]
            .strip("'\"\n ")
        )
    return version


class Test_framework:
    def test_version(self):
        assert typer_demo.__version__ == get_pyproject_version()

    def test_version_metadata(self):
        pytest.skip(
            reason="Don't understand .metadata.version() issue \
            where we need to put \
            missing 1 required positional argument: 'distribution_name'"
        )  # TODO: GEN-42 https://kodekeith.atlassian.net/browse/GEN-42
        assert (
            typer_demo.__version__
            == get_pyproject_version()
            == importlib.metadata.version()
        )

    def test_summer(self):
        print(summer(2, 4))
        assert summer(1, 4) == 5


def test_fail_example():
    pytest.skip(
        reason="Don't understand to point of the fail as it still makes a fail!"
    )
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


# def test_exit_example():
#     # old
#     # pytest.exit(msg="foo")
#     # new
#     assert True
#     pytest.exit(reason="bar")
