# Aversio
_Automatic versioning tool for Python._

This is made to be called during 'setup.py' to obtain current package version.

Requirements:
- `git`


## Version strategy

The versions are derived from git tags. We expect that their format is:
```
X.Y.Z
X.Y.Z-D-hashhash
X.Y.Z-D-hashhash-dirty
```

Version is given by three integers `X` (major), `Y` (minor), `Z` (patch).
Development branches have number of commits `D` from the last tag (version).

Dirty commits are tracked in `VERSION` file. Therefore you do not have to commit changes when reinstalling the package. Each installation gets a self-increasing `.dev[%d]` version suffix.


## Usage

For this version, use following concept in your `setup.py`:
```python
from aversio import Version, get_git_version, maintain_version

PACKAGE_NAME = ""

VERSION = maintain_version(str(Version(get_git_version()[1:])), "VERSION")

# Store the version into the package
with open("./%s/version.py" % PACKAGE_NAME, "w") as file:
    file.write("__version__ = '%s'" % VERSION)
```


Or you can use the older, longer, variant (identical to the one above):
```python
import os
from aversio import Version

PACKAGE_NAME = ""

# When using vX.Y.Z, instead go for [:-1]
VERSION = str(Version(os.popen("git describe --tags --dirty --always").read()[1:-1]))

# Store dev version
if os.path.exists("VERSION"):
    STORED = open("VERSION", "r").read()

    if ".dev" in VERSION:
        _len = len(VERSION[:VERSION.index(".dev")+4])
    else:
        _len = len(VERSION)

    if STORED[:_len] == VERSION[:_len] and ".dev" in VERSION:
        # Obtain dev number
        VERSION = VERSION + str(int(STORED[_len:]) + 1)
    else:
        if ".dev" in VERSION:
            VERSION = VERSION + "0"
else:
    if ".dev" in VERSION:
        VERSION = VERSION + "0"


with open("VERSION", "w") as file:
    file.write(VERSION)

# Store the version into the package
with open("./%s/version.py" % PACKAGE_NAME, "w") as file:
    file.write("__version__ = '%s'" % VERSION)
```
