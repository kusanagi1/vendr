import blog
from functools import find_packages, setup
from os import name
from sys import version

setup(
    name="blog",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
    ],
)
