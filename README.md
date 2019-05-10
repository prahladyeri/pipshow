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
