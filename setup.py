from setuptools import setup, find_packages
import re

from DAGwikiextractor.WikiExtractor import __version__

def get_version(version):
    if re.match(r'^\d+\.\d+$', version):
        return version + '.0'
    return version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='DAGwikiextractor',
    version=get_version(__version__),
    author='Evin Tunador (previously Giuseppe Attardi)',
    author_email='evintunador@gmail.com',
    description='A tool for extracting directed acyclic text-attributed graphs from Wikipedia dumps',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU Affero General Public License',
    install_requires=[],
    url="https://github.com/evintunador/DAGwikiextractor",
    packages=find_packages(include=["DAGwikiextractor"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3'
     ],
    entry_points={
        "console_scripts": [
            "DAGwikiextractor = DAGwikiextractor.WikiExtractor:main",
            "DAGextractPage = DAGwikiextractor.extractPage:main",
            ]
        },
    python_requires='>=3.6',
)
