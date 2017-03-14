# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.2.3'
long_description = '\n'.join([
        open(os.path.join("src", "README.txt")).read(),
        open(os.path.join("src", "AUTHORS.txt")).read(),
        open(os.path.join("src", "HISTORY.txt")).read(),
        ])

classifiers = [
    "Development Status :: 4 - Beta",
    "Framework :: Sphinx :: Theme",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
    name='sphinxjp.themes.tinkerturquoise',
    version=version,
    description='Two column blogging theme tool for Tinkerer, based on turquoise color.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['tinkerer', 'sphinxjp', 'reStructuredText', 'theme'],
    author='nao iwata',
    author_email='orrrizzle{at}gmail.com',
    url='https://github.com/naoiwata/sphinxjp.themes.tinkerturquoise',
    license='MIT',
    namespace_packages=['sphinxjp', 'sphinxjp.themes'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['buildout.cfg']},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'docutils',
        'tinkerer',
        'sphinxjp.themecore',
        'pygments-style-solarized',
    ],
    entry_points="""
        [sphinx_themes]
        path = sphinxjp.themes.tinkerturquoise:template_path

    """,
    zip_safe=False,
)
