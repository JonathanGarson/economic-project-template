from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1.0',
    packages=find_packages(),
    author='{{ cookiecutter.author_name }}',
    license='{{ cookiecutter.open_source_license }}')