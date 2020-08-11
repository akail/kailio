# -*- coding: utf-8 -*-

import pytest

from kailio import __version__, create_app, db as _db


@pytest.fixture(scope='session')
def client():
    app = create_app('.test_env')

    with app.test_client() as client:
        with app.app_context():
            _db.create_all()
        yield client

    with app.app_context():
        _db.drop_all()
