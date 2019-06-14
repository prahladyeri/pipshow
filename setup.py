import os
from setuptools import setup, find_packages
from pipshow import __version__, __description__, __author__, __email__, __license__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="pipshow",
	version=__version__,
	license=__license__,
	description=__description__,
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
	author=__author__,
	author_email=__email__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	
)