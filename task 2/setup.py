#!/usr/bin/env python3.9
"""Setup serializer."""
from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='serializer',
    version='1.0',
    description='Application to serailize, deserialize ',
    author='Kalinina Ekaterina',
    packages=['serializer', 'test'],
    scripts=['cereal']
)