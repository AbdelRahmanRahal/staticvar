from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.0.5"
DESCRIPTION = "The horrors of C Static variables for Python, made with Python."
THIS_DIRECTORY = Path(__file__).parent
LONG_DESCRIPTION = (THIS_DIRECTORY / "README.md").read_text(encoding = "utf8")

setup(
        name = "StaticVar", 
        version = VERSION,
        author = "AbdelRahman Rahal",
        author_email = "<abdelrahman.rahal.mail@gmail.com>",
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        long_description_content_type = "text/markdown",
        url = "https://github.com/AbdelRahmanRahal/StaticVar",
        project_urls = {
            'Repository': "https://github.com/AbdelRahmanRahal/StaticVar"
        },
        packages = find_packages(),
        install_requires = ["varname"],
        python_requires = ">=3.10",

        
        keywords=["Static", "Static Variables", "StaticVar"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)