# setup.py
from setuptools import setup, find_packages

setup(
    name="omni-ruff",
    version="0.5.1",
    packages=find_packages(include=["hooks.*"]),
    python_requires=">=3.9",
    author="Steven Ramdas",
    entry_points={
        "console_scripts": [
            "copy-ruff-config=hooks.copy_ruff_config:main",
            "clone-ruff-config=hooks.clone_ruff_config:main"
        ],
    },
)
