'''
Covasim installation. Requirements are listed in requirements.txt. There are two
options:
    python setup.py develop      # standard install, does not include optional libraries
    python setup.py develop full # full install, including optional libraries (NB: these libraries are not available publicly yet)
'''

import os
import sys
import runpy
from setuptools import setup, find_packages

# Load requirements from txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if 'full' in sys.argv:
    print('Performing full installation, including optional dependencies')
    sys.argv.remove('full')
    full_reqs = [
        'plotly',
        'fire',
        'synthpops',
        'parestlib',
    ]
    requirements.extend(full_reqs)

# Get version
cwd = os.path.abspath(os.path.dirname(__file__))
versionpath = os.path.join(cwd, 'covasim', 'version.py')
version = runpy.run_path(versionpath)['__version__']

# Get the documentation
with open(os.path.join(cwd, 'README.rst'), "r") as f:
    long_description = f.read()

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: Other/Proprietary License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3.7",
]

setup(
    name="covasim",
    version=version,
    author="Cliff Kerr, Robyn Stuart, Romesh Abeysuriya, Dina Mistry, Lauren George, and Daniel Klein, on behalf of the IDM COVID-19 Response Team",
    author_email="covasim@idmod.org",
    description="COVID-19 Agent-based Simulator",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='http://covasim.org',
    keywords=["Covid-19", "coronavirus", "SARS-CoV-2", "stochastic", "agent-based model", "interventions", "epidemiology"],
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)

