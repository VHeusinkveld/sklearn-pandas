#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.test import test as TestCommand
import re

for line in open('sklearn_pandas/__init__.py'):
    match = re.match("__version__ *= *'(.*)'", line)
    if match:
        __version__, = match.groups()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        raise SystemExit(errno)


setup(name='sklearn-pandas2',
      version=__version__,
      description='Pandas integration with sklearn',
      maintainer='Ritesh Agrawal',
      maintainer_email='ragrawal@gmail.com',
      url='https://github.com/ragrawal/sklearn-pandas',
      packages=['sklearn_pandas2'],
      keywords=['scikit', 'sklearn', 'pandas'],
      install_requires=[
          'scikit-learn>=0.15.0',
          'scipy>=0.14',
          'pandas>=0.11.0',
          'numpy>=1.6.1',
          'tqdm>=4.46.0'],
      tests_require=['pytest', 'mock'],
      cmdclass={'test': PyTest},
      )
