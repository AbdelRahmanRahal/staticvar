from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Static variables for Python'
LONG_DESCRIPTION = 'Static variables for Python like in C'

setup(
        name="StaticVar", 
        version=VERSION,
        author="AbdelRahman Rahal",
        author_email="<abdelrahman.rahal.mail@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['varname'],
        python_requires=">=3.10",
        
        keywords=['Static', 'Static Variables', 'StaticVar'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3 :: Only",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)