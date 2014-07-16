#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0-dev"

try:
    __TRANSIT_SETUP__
except NameError:
    __TRANSIT_SETUP__ = False

if not __TRANSIT_SETUP__:
    __all__ = ["ldlc_simple", "System", "Central", "Body"]

    from ._transit import ldlc_simple
    from .model import System, Central, Body
