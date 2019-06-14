![pypi](https://img.shields.io/pypi/v/pipshow.svg)
![python](https://img.shields.io/pypi/pyversions/pipshow.svg)
![implementation](https://img.shields.io/pypi/implementation/pipshow.svg)
<!-- https://img.shields.io/travis/prahladyeri/pipshow/master.svg -->
<!-- ![docs](https://readthedocs.org/projects/pipshow/badge/?version=latest) -->
![license](https://img.shields.io/github/license/prahladyeri/pipshow.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/pipshow.svg)
<!--![commit-activity](https://img.shields.io/github/commit-activity/w/prahladyeri/pipshow.svg)-->
[![donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JM8FUXNFUK6EU)
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)
# pipshow

A script to show details of any python package, irrespective of whether its installed or not.

# Synopsis

I came across the need today to show details about a random PyPi package which wasn't installed on my machine yet. So I simply did `pip show <package_name>` but it didn't return anything. `pip` has also removed the `--no-install` option for simulating an install through which I could have known these details too. So I wrote this little script to show the details of any package even if it isn't installed on your machine.

# Installation

```bash
pip install pipshow
```

# Usage

```bash
> pipshow pipshow
Name: pipshow
Version: 0.5
Summary: A script to show details of any python package, irrespective of whether its installed or not.
Home-page: https://github.com/prahladyeri/pipshow
Package URL: https://pypi.org/project/pipshow/
Author: Prahlad Yeri
Author-email: prahladyeri@yahoo.com
License: MIT
Requires: None
```