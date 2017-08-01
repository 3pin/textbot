#from distutils.core import setup
from setuptools import setup

setup(
    # Application name:
    name="textbot",

    # keywords
    keywords = ["NLP", "IE", "wordnet", "nltk"],

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="3pin",
    author_email="3pin.audiovisual@gmail.com",

    # Details
    url='http://github.com/3pin/textbot',
    license="LICENSE.txt",
    description="Read a column of strings from csv, parse wordnet pos_tags to lemmas, enumerate most_common lemmas, weight strings via top scoring lemmas",
    long_description=open("README.txt").read(),

    # minimum python version
    python_requires='>=3',

    # Dependent packages (distributions)
    install_requires=["tkinter.filedialog","tkinter.simpledialog","pandas","nltk","re","json","operator","collections","string","UnicodeDammit","bs4"],

    # Packages
    packages=["textbot"],
    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),


    # Include additional files into the package
    include_package_data=True,

    # include specific data files into the above packages
    #package_data={'sample': ['package_data.dat'],},

    # include data outside of the included packages
    #data_files=[('my_data', ['data/data_file'])],

    # classify your app on the PyPI database
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: General",
        ],


)
