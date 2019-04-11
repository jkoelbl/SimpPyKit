from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
   name='SimpPyKit',
   version='0.1',
   description='Package containing wrapper functions and classes for ease of use',
   license='',
   long_description=long_description,
   author='Jordan Koelbl',
   author_email='',
   url='http://github.com/jkoelbl/SimpPyKit',
   packages=['SimpPyKit'],         #same as name
   install_requires=[],     #external packages as dependencies
   scripts=[]
)
