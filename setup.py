#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:08:21 2019

@author: 278mt
"""

from setuptools import setup
from bibdoigetter import __version__

setup(
    name="bibdoigetter",
    version=__version__,
    packages=["requests","bs4"],
    )