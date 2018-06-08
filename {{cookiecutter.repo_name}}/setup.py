import os
import re
from codecs import open
from setuptools import setup, find_packages


def get_version(*file_paths):
    """Retrieves the version from {{ cookiecutter.app_name }}/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

version = get_version("{{ cookiecutter.app_name }}", "__init__.py")
install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='{{cookiecutter.app_name}}',
    version=version,
    description='{{cookiecutter.project_short_description}}',
    long_description=readme,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    license="{{ cookiecutter.open_source_license }}",
    classifiers=[
        'Intended Audience :: Developers',{% if '1.11' in cookiecutter.django_versions %}
        'Framework :: Django :: 1.11',{% endif %}{% if '2.0' in cookiecutter.django_versions %}
        'Framework :: Django :: 2.0',{% endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
)
