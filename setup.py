#!/usr/bin/env python

from setuptools import setup

import os

# NOTE(drozdziak1): Hardcoded for PBR
os.environ["PBR_VERSION"] = "6.3.1-pbr-devdep"

setup(
    setup_requires=['pbr'],
    pbr=True,
)
