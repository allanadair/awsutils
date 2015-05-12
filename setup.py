#!/usr/bin/env python
"""
Setup.py script for awsutils

"""
from setuptools import setup, find_packages
import awsutils


def readme(filepath):
    """
    Returns contents of a readme file.

    """
    with open(filepath, 'r') as rm:
        return rm.read()

requires = ['awscli']

setup_options = dict(name='awsutils',
                     version=awsutils.__version__,
                     description='Utilities for managing Amazon ec2 instances based "Name" tags as unique identifiers',
                     license='BSD',
                     long_description=readme('README.rst'),
                     author='Allan Adair',
                     author_email='allan.m.adair@gmail.com',
                     url='https://github.com/allanadair/awsutils',
                     scripts=['scripts/awssh.py'],
                     packages=find_packages('.'),
                     package_dir={'awsutils': 'awsutils'},
                     install_requires=requires,
                     classifiers=('Development Status :: 1 - Planning',
                                  'Intended Audience :: Developers',
                                  'Intended Audience :: System Administrators',
                                  'Natural Language :: English',
                                  'License :: OSI Approved :: BSD License',
                                  'Programming Language :: Python',
                                  'Programming Language :: Python :: 2.6',
                                  'Programming Language :: Python :: 2.7',
                                  'Programming Language :: Python :: 3',
                                  'Programming Language :: Python :: 3.4'))

setup(**setup_options)
