from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecocuivre/__init__.py
from ecocuivre import __version__ as version

setup(
	name="ecocuivre",
	version=version,
	description="customisations for Ecocuivre",
	author="Ecocuivre",
	author_email="contact@ecocuivre.dz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
