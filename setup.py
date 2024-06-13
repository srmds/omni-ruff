# setup.py
from setuptools import setup, find_packages

setup(
    name="omni-ruff",
    version="0.2.0",
    packages=find_packages(),
    author="Steven Ramdas",
    entry_points={
        "console_scripts": [
            "copy-ruff-config=copy_ruff_config:main",
            "clone-ruff-config=clone_ruff_config:main"
        ],
    },
)
