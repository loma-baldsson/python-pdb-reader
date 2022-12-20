# template from pypa's sample project
# https://raw.githubusercontent.com/pypa/sampleproject/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="pypalm",
    version="0.0.1a1",  # Required
    description="A (currently unfinished) python interface for the Palm DB format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loma-baldsson/python-pdb-reader",
    author="loma-baldsson",
    author_email="howtopoopin2021official@gmail.com",
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Embedded Systems",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="palm, palmos, palm os, pdb",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10, <4",
    extras_require={  # Optional
        "test": ["pytest"],
    },
    project_urls={
        "Bug Reports": "https://github.com/loma-baldsson/python-pdb-reader/issues",
    },
)
