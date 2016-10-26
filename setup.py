import sys

from setuptools import setup, find_packages

requires = ['slave']

desc = ('An implementation of the LakeShore 336 Model')

setup(
    name='lakeshore336',
    version=__import__('lakeshore336').__version__,
    author='Alexander Book',
    author_email='alexander.book@frm2.tum.de',
    license = 'GNU General Public License (GPL), Version 3',
    url='https://github.com/TUM-E21-ThinFilms/lakeshore336',
    description=desc,
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
