#!/usr/bin/env python
# _version.py
"""Script for managing versions."""

import os

def get_git_version():
    """Obtain the git version of the current folder.

    Returns:
    git_version -- current git version, str
    """
    return os.popen("git describe --tags --dirty --always").read()[:-1]


def fix_version(version, stored_version = ""):
    """Format and obtain the true version by comparing the latest one with current.

    Arguments:
    version -- current version, str
    stored_version -- latest stored version, str

    Returns:
    fixed_version -- current true version, str
    """

    if stored_version != "":
        if ".dev" in version:
            _len = len(version[:version.index(".dev")+4])
        else:
            _len = len(version)

        if stored_version[:_len] == version[:_len] and ".dev" in version:
            # Obtain dev number
            version = version + str(int(stored_version[_len:]) + 1)
        else:
            if ".dev" in version:
                version = version + "0"
    else:
        if ".dev" in version:
            version = version + "0"

    return version


def maintain_version(version, filename = "VERSION"):
    """Fix version according to the stored one.

    Arguments:
    version -- current version, str
    filename -- name of the file with latest version, str

    Returns:
    version -- current true version, str

    Note: This just reads the file, runs 'fix_version' and
    saves the result.
    """
    stored = ""

    if os.path.exists(filename):
        stored = open(filename, "r").read()

    version = fix_version(version, stored)

    with open(filename, "w") as file:
        file.write(version)

    return version


class Version():
    """Simple class for parsing versions and creating a Py-compatible format.

    We take into account following types:
    1.0.0
    1.0.0-1-1578sdfe
    1.0.0-1-1484fdgd-dirty
    """

    def __init__(self, git_version):
        version = (git_version if "-" not in git_version else git_version[:git_version.index("-")]).split(".")

        self.MAJOR = version[0]
        self.MINOR = version[1]
        self.PATCH = version[2] if len(version) > 2 else None

        _git_version = git_version

        # Dirty
        if "-" in _git_version:
            _git_version = _git_version[_git_version.index("-")+1:]

            self.DEV = _git_version[-5:] == "dirty"

            if self.DEV:
                _git_version = _git_version[:-6]
        else:
            self.DEV = False

        # Commit
        self.POSTPATCH = None
        if len(_git_version) > 0 and "-" in _git_version:
            self.POSTPATCH = _git_version[:_git_version.index("-")]
            _git_version = _git_version[_git_version.index("-")+1:]

        # Save the commit / tag version
        if _git_version != "":
            self.OTHER = _git_version
        else:
            self.OTHER = git_version[:-6] if self.DEV else git_version


    def __str__(self):
        return "%s.%s" % (self.MAJOR, self.MINOR) + (".%s" % self.PATCH if self.PATCH else "") + (".post%s" % self.POSTPATCH if self.POSTPATCH else "") + (".dev" if self.DEV else "")


    def __repr__(self):
        return self.__str__() + " (" + self.OTHER + ")"
