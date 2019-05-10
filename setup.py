from setuptools import setup, find_packages

setup(
	name="pipshow",
	version="0.1",
	license="MIT",
	description="script to show details of any pip package, irrespective of whether its installed or not.",
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