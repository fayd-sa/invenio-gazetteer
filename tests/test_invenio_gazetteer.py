# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 FAYD.
#
# Invenio-Gazetteer is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_gazetteer import InvenioGazetteer


def test_version():
    """Test version import."""
    from invenio_gazetteer import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioGazetteer(app)
    assert 'invenio-gazetteer' in app.extensions

    app = Flask('testapp')
    ext = InvenioGazetteer()
    assert 'invenio-gazetteer' not in app.extensions
    ext.init_app(app)
    assert 'invenio-gazetteer' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Invenio-Gazetteer' in str(res.data)
