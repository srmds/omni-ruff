# setup.py
from setuptools import setup, find_packages
from os import path

current_directory = path.abspath(path.dirname(__file__))
with open(path.join(current_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name='omni-ruff',
    version='0.1',
    packages=find_packages(include=["hooks.*"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Steven Ramdas",
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'copy-ruff-config=hooks.copy_ruff_config:main',
        ],
    },
)
