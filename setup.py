from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tresorerie/__init__.py
from tresorerie import __version__ as version

setup(
	name="tresorerie",
	version=version,
	description="Un logiciel de gestion de caisse",
	author="Basil BANZA",
	author_email="basil.banza@outlook.com.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
