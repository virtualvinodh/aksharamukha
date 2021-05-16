"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

import io

with io.open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

setup(
  name='aksharamukha',

  # Versions should comply with PEP440.  For a discussion on single-sourcing
  # the version across setup.py and the project code, see
  # https://packaging.python.org/en/latest/single_source_version.html
  version='@@@',

  description='Provides script conversion (a.k.a transliteration) between scripts within the Indic cultural sphere',
  long_description=long_description,
  long_description_content_type='text/markdown',

  # The project's main homepage.
  url='https://github.com/@@@/aksharamukha',

  # Author details
  author='Vinodh Rajan',
  author_email='vinodh@virtualvindh.com',

  # Choose your license
  license='GNU AGPL 3.0',

  # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',

    'Natural Language :: Tamil',
    'Natural Language :: Telugu',
    'Natural Language :: Hindi',
    'Natural Language :: Marathi',

    'Natural Language :: Bengali',
    'Natural Language :: Urdu',
    'Natural Language :: Thai',
    'Natural Language :: Tibetan',

    'Topic :: Text Processing :: Linguistic',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: GNU Affero General Public License v3',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],

  # What does your project relate to?
  keywords='unicode indic indian language script brahmi brahmic asian transliteration conversion writing alphabet romanization',

  # You can just specify the packages manually here if your project is
  # simple. Or you can use find_packages().
  packages=find_packages(),

  # Alternatively, if you want to distribute just a my_module.py, uncomment
  # this:
  #   py_modules=["my_module"],

  # List run-time dependencies here.  These will be installed by pip when
  # your project is installed. For an analysis of "install_requires" vs pip's
  # requirements files see:
  # https://packaging.python.org/en/latest/requirements.html
  install_requires=['requests'],

  # List additional groups of dependencies here (e.g. development
  # dependencies). You can install these using the following syntax,
  # for example:
  # $ pip install -e .[dev,test]
  # If there are data files included in your packages that need to be
  # installed, specify them here.  If using Python 2.6 or less, then these
  # have to be included in MANIFEST.in as well.
  # package_data={
  #     'sample': ['package_data.dat'],
  # },

  # Although 'package_data' is the preferred approach, in some case you may
  # need to place data files outside of your packages. See:
  # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
  # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
  # data_files=[('my_data', ['data/data_file'])],

  # To provide executable scripts, use entry points in preference to the
  # "scripts" keyword. Entry points provide cross-platform support and allow
  # pip to create the appropriate form of executable for the target platform.
  # entry_points={
  #     'console_scripts': [
  #         'sample=sample:main',
  #     ],
  # },
)
