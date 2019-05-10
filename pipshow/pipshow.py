import requests
import json
import argparse

def fileexists(filepath):
	try:
		if os.path.isfile(filepath):
			return filepath
		else:
			print("There is no file at:" + filepath)
			exit()
	except e as Exception:
			print(e)

def main():
	parser = argparse.ArgumentParser(description="Pypi package name to get the info.")
	#parser.add_argument("input", type=fileexists, help='Input File Location EX: /Desktop/Somewhere/input.txt')
	parser.add_argument("input", help='Name of the package EX: Foo')
	args = parser.parse_args()
	
	url = 'https://pypi.org/pypi/{}/json'
	try:
		obj = requests.get(url.format(args.input)).json()
		print("Name: %s" % (obj['info']['name']))
		print("Version: %s" % (obj['info']['version']))
		print("Summary: %s" % (obj['info']['summary']))
		print("Home-page: %s" % (obj['info']['home_page']))
		print("Package URL: %s" % (obj['info']['package_url']))
		print("Author: %s" % (obj['info']['author']))
		print("Author-email: %s" % (obj['info']['author_email']))
		print("License: %s" % (obj['info']['license']))
		print("Requires: %s" % (obj['info']['requires_dist']))
	except Exception as ex:
		print("Error occurred. Please check whether the package name is correct.")
		print("Error Text: ", str(ex))

if __name__ == "__main__":
	main()