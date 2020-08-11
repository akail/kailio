# -*- coding: utf-8 -*-

import pytest

from kailio import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_app(client):
    rv = client.get('/')
    assert rv.status_code == 200
