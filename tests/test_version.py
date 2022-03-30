#!/usr/bin/env python
# test_version.py
"""Test various git versions whether they are parsed properly.
"""
######################
# Imports & Globals
######################

import unittest

from aversio import Version


######################
# Utilities
######################

def assertVersion(obj, ver_obj, commit, major, minor, patch = None, dev = False, postpatch = None):
    obj.assertEqual(ver_obj.MAJOR, str(major))
    obj.assertEqual(ver_obj.MINOR, str(minor))
    obj.assertEqual(ver_obj.PATCH, str(patch) if patch else patch)
    obj.assertEqual(ver_obj.DEV, dev)
    obj.assertEqual(ver_obj.POSTPATCH, str(postpatch) if postpatch else postpatch)
    obj.assertEqual(ver_obj.OTHER, str(commit))


######################
# Tests
######################

class OrdinaryVersion(unittest.TestCase):

    def test_XY(self):
        """Test parsing of X.Y version.
        """
        assertVersion(self, Version("2.3"), "2.3", 2, 3)

    def test_XYd(self):
        """Test parsing of X.Y-dirty version.
        """
        assertVersion(self, Version("2.3-dirty"), "2.3", 2, 3, dev = True)


    def test_XYZ(self):
        """Test parsing of X.Y.Z version.
        """
        assertVersion(self, Version("3.4.5"), "3.4.5", 3, 4, 5)


    def test_XYZd(self):
        """Test parsing of X.Y.Z-dirty version.
        """
        assertVersion(self, Version("3.4.5-dirty"), "3.4.5", 3, 4, 5, dev = True)


    def test_XYZDh(self):
        """Test parsing of X.Y.Z-D-hhhhhhhh version.
        """
        assertVersion(self, Version("3.4.6-9-abcdefgh"), "abcdefgh", 3, 4, 6, postpatch = 9)


    def test_XYZDhd(self):
        """Test parsing of X.Y.Z-D-hhhhhhhh-dirty version.
        """
        assertVersion(self, Version("3.4.6-9-abcdefgh-dirty"), "abcdefgh", 3, 4, 6, postpatch = 9, dev = True)


######################
# Main
######################

if __name__ == '__main__':
    unittest.main()
