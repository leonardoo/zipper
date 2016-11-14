# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

install_requires = []
if (sys.version_info[0], sys.version_info[1]) < (3, 2):
    install_requires.append('pathlib2')

setup(
    name='zipper',
    version='0.0.1',
    description='Zipper',
    author='leonardo orozco',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.tests']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities'
    ]
)
