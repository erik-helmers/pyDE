"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from pyDE import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=pyDE', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='pyDE',
    version=__version__,
    description='Another IDE for Python.',
    long_description=long_description,
    url='https://github.com/erik-helmers/pyDE',
    author='Erik Helmers',
    author_email='erik.helmers@outlook.fr',
    license='UNLICENSE',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: UNIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='ide',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt', 'pyqt5'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'pyDE = pyDE.main:main',
        ],
    },
    cmdclass={'test': RunTests},
)
