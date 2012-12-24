#!/usr/bin/python3
"""This script builds ns-3-nat."""
__author__ = "Takashi SASAKI <takashi316@gmail.com>"
__date__ = "Dec. 24, 2012"

import os
import pydoc

if __name__ == "__main__":
    os.system("cd openflow; ./waf clean")
    os.system("cd openflow; ./waf configure")
    os.system("cd openflow; ./waf")
    os.system("cd ns-3-nat; ./waf clean")
    os.system("cd ns-3-nat; ./waf configure --enable-tests --enable-examples")
    os.system("cd ns-3-nat; ./waf")
    os.system("cd ns-3-nat; ./test.py")
 
