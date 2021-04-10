#!/usr/bin/env python3
"""Setup file to package imu_generator."""

import pipfile
from setuptools import find_packages, setup

# pipfile: when using pipenv, get the dependencies listed in Pipfile
PF = pipfile.load('Pipfile')
PFLIST = [
    ('{}{}'.format(pkg_name, version) if version != '*' else pkg_name)
    for pkg_name, version in PF.data['default'].items()
]

setup(
    name='imu_generator',
    description='Python program for me',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Macos',
        'Intended Audience :: Developers',
        'Natural Language :: English, French',
        'Programming Language :: Python 3',
    ],
    author='Thibaut Grall',
    author_email='_',
    url='_',
    #
    # Find_packages helps finding (python) files and packages to include,
    # provided __init__.py files are present in the directories.
    # cf. https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages
    packages=find_packages(),
    # External packages required by the project
    # Either use an explicit list, or rely on pipfile package
    # cf. https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies
    install_requires=PFLIST,
    #
    # Declare a few console scripts
    # When the package is installed by root, those will be found in /usr/local/bin
    entry_points={
        'console_scripts': [
            'imu_generator',
        ],
    },
    #
    # Set package version according to git commits and tags
    # root is the location of the .git directory
    use_scm_version={
        'root': '',
        'relative_to': __file__,
    },
    setup_requires=['setuptools_scm'],
)
