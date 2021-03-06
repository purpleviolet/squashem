#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `squashem` package."""

import pytest

from click.testing import CliRunner

from squashem.squashem import squashem
from squashem import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_squashem_function():
    matrix = [[1, 2, 3], [4, 5, 6]]
    new_list = squashem(matrix)
    assert new_list == [1, 2, 3, 4, 5, 6]


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'squashem.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
