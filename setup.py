
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='togglee',
    version='0.0.1',
    description='Simple toggles for python from a url reference',
    long_description=readme,
    author='Kanekotic',
    author_email='me@kanekotic.com',
    url='https://github.com/togglee/togglee-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)