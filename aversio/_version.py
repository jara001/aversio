#!/usr/bin/env python
# _version.py
"""Script for managing versions."""

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
