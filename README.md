![pypi](https://img.shields.io/pypi/v/distroverify.svg)
![python](https://img.shields.io/pypi/pyversions/distroverify.svg)
![implementation](https://img.shields.io/pypi/implementation/distroverify.svg)
<!-- https://img.shields.io/travis/prahladyeri/distroverify/master.svg -->
<!-- ![docs](https://readthedocs.org/projects/distroverify/badge/?version=latest) -->
![license](https://img.shields.io/github/license/prahladyeri/distroverify.svg)
![last-commit](https://img.shields.io/github/last-commit/prahladyeri/distroverify.svg)
<!--![commit-activity](https://img.shields.io/github/commit-activity/w/prahladyeri/distroverify.svg)-->
[![follow](https://img.shields.io/twitter/follow/prahladyeri.svg?style=social)](https://twitter.com/prahladyeri)
# pipshow

A script to show details of any python package, irrespective of whether its installed or not.

# Synopsis

I came across the need today to show details about a random PyPi package which wasn't installed on my machine yet. So I simply did `pip show <package_name>` but it didn't return anything. `pip` has also removed the `--no-install` option for simulating an install through which I could have known these details too. So I wrote this little script to show the details of any package even if it isn't installed on your machine.

# Installation
```
pip install pipshow
```

# Usage

![Usage](https://github.com/prahladyeri/pipshow/blob/master/screenshot.png?raw=true)

# Uninstallation
```pip uninstall pipshow```
