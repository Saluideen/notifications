from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in notifications/__init__.py
from notifications import __version__ as version

setup(
	name="notifications",
	version=version,
	description="Notifications",
	author="Ideen",
	author_email="salu@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
