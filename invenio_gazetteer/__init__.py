# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 FAYD.
#
# Invenio-Gazetteer is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for indexing and previewing LinkedPlaces JSON files."""

from .ext import InvenioGazetteer
from .version import __version__

__all__ = ('__version__', 'InvenioGazetteer')
