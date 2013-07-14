from distutils.core import setup

setup(
    name='MulchPy',
    version='0.1.0',
    author='Wil L. Hall',
    author_email='wil@wilhall.com',
    packages=['mulchpy', 'mulchpy.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/MulchPy/',
    license='LICENSE.txt',
    description='The Mulch Chemistry Stoichiometry C++ Library, ported to Python',
    long_description=open('README.txt').read(),
    install_requires=[],
)