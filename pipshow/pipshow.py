import json, sys
import argparse
import urllib.parse
import requests

def show_extra_stats(repo):
	# soup = BeautifulSoup(resp.text,'lxml')
	# info = soup.select(".github-repo-info")
	# if info != None:
		# info[0].select('[data-supplement="/stargazers"]')
	uname = repo.split("/")[0]
	resp = requests.get("https://api.github.com/users/{uname}/repos".format(uname=uname))
	obj = json.loads(resp.text)
	for item in obj:
		if item['full_name'] == repo:
			print("\nGITHUB STATS:")
			print("stars: %d" % item['stargazers_count'])
			print("forks: %d" % item['forks_count'])
			print("open_issues: %d" % item['open_issues'])	
			print("last_commit: %s" % item['updated_at'])

def main():
	args = sys.argv[1:]
	parser = argparse.ArgumentParser()
	#parser.add_argument("input", type=fileexists, help='Input File Location EX: /Desktop/Somewhere/input.txt')
	parser.add_argument("input", help='Name of the package EX: Foo')
	parser.add_argument('-s', "--stats", action='store_true', help='Show extra stats from github')
	
	args = parser.parse_args(args)
	
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
		#print("Requires: %s" % (obj['info']['requires_dist']))
		if args.stats:
			parts = urllib.parse.urlparse(obj['info']['home_page'])
			if parts.netloc == 'github.com':
				show_extra_stats(parts.path.strip("/"))
			else:
				print("This package doesn't have a github repo")
	except Exception as ex:
		print("Error occurred. Please check whether the package name is correct.")
		print("Error Text: ", str(ex))

if __name__ == "__main__":
	main()
