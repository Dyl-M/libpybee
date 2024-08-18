# -*- coding: utf-8 -*-

"""File Information
@file_name: setup.py
@author: Dylan "dyl-m" Monfret
Setup for deployment
"""

import setuptools
import shutil
import subprocess


def get_version_from_git():
    """Retrieve package version from git tag name.
    @return: package version.
    """
    git_path = shutil.which("git")

    if git_path is None:
        raise EnvironmentError("Git is not installed or not found in PATH.")

    try:
        version = subprocess.check_output(['git', 'describe', '--tags']).strip().decode('utf-8').split('-')[0]
        return version

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Failed to get version from git: {error}")


def parse_requirements():
    """Load requirements from a pip requirements file and return them as a list
    @return: dependencies with compatibility symbol changed
    """
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip().replace('~=', '>=')
                for line in f if line.strip() and not line.startswith("#")]


setuptools.setup(
    name='libpybee',
    version=get_version_from_git(),
    author='Dylan "dyl-m" Monfret',
    author_email="dyl_m.dev@proton.me",
    description='MusicBee Library Parser in Python (based on Liam Kaufman\'s "libpytunes")',
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
    }
)

