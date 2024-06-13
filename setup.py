# setup.py
from setuptools import setup, find_packages

setup(
    name='omni-ruff',
    package_dir={'': '.'},
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hooks.copy_ruff_config',
        ],
    },
)
