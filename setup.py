import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="pipshow",
	version="0.5",
	license="MIT",
	description="A script to show details of any python package, irrespective of whether its installed or not.",
	long_description=read("README.md"),
	long_description_content_type='text/markdown',
	keywords="pip,setup,installer",
	url="https://github.com/prahladyeri/pipshow",
	packages=find_packages(),
	#scripts=['pipshow.py'],
	entry_points={
		"console_scripts": [
			"pipshow = pipshow.pipshow:main",
		],
	},
	install_requires=['requests'],
	# package_data = {
		# 'pipshow': ['./'],
	# },
	author="Prahlad Yeri",
	author_email="prahladyeri@yahoo.com",
	
)