# -*- coding: utf-8 -*-

"""File Information
@file_name: setup.py
@author: Dylan "dyl-m" Monfret
Setup for deployment
"""

import setuptools
import subprocess


def get_version_from_git():
    """Retrieve package version from tag name
    @return: package version.
    """
    version = subprocess.check_output(["git", "describe", "--tags"]).strip().decode("utf-8")
    return version


def parse_requirements(r_filename: str):
    """Load requirements from a pip requirements file and return them as lists
    @param r_filename: path to text requirements file
    @return: lists of requirements, basic and extra requirements.
    """
    with open(r_filename, 'r', encoding='utf-8') as f:
        return [line.strip().replace('~=', '>=')
                for line in f if line.strip() and not line.startswith("#")]


setuptools.setup(
    name='libpybee',
    version=get_version_from_git(),
    author='Dylan "dyl-m" Monfret',
    author_email="dyl_m.dev@proton.me",
    description="A Python package for managing MusicBee library data.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dyl-M/libpybee",
    packages=setuptools.find_packages(),
    package_data={"libpybee": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["libpybee = libpybee.main:main"]},
    install_requires=parse_requirements(),
    extras_require={
        "dev": [
            "flakes",
            "pytest",
            "pytest-cov"
        ]
    },
    test_suite="_tests",
)
