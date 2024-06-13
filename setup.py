# setup.py
from setuptools import setup, find_packages
from os import path

setup(
    name="omni-ruff",
    version="0.1",
    packages=find_packages(include=["hooks.*"]),
    author="Steven Ramdas",
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "copy-ruff-config=hooks.copy_ruff_config",
        ],
    },
)
