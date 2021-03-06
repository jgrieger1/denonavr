#!/usr/bin/env python
# encoding: utf-8
"""Automation Library for Denon AVR receivers."""
from setuptools import find_packages, setup

setup(name='denonavr',
      version='0.5.5+griegers',
      description='Automation Library for Denon AVR receivers',
      long_description='Automation Library for Denon AVR receivers',
      url='https://github.com/jgrieger1/denonavr@AVR4310',
      author='Oliver Goetz',
      author_email='scarface@mywoh.de',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests'],
      tests_require=['tox'],
      platforms=['any'],
      zip_safe=False,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries",
          "Topic :: Home Automation",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          ])
