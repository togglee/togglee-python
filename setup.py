import os
import pypandoc
from setuptools import setup, find_packages

pypandoc.download_pandoc()
long_description = pypandoc.convert_file('README.md', 'rst')

with open('LICENSE') as f:
    license = f.read()

with open('requirements_prod.txt') as f:
    required = f.read().splitlines()

setup(
    name='togglee',
    version=f'0.0.{os.getenv("GITHUB_RUN_NUMBER", "1-SNAPSHOT")}',
    description='Simple toggles for python from a url reference',
    long_description=long_description,
    author='kanekotic',
    author_email='me@kanekotic.com',
    url='https://github.com/togglee/togglee-python',
    install_requires=required,
    license=license,
    packages=find_packages()
)
