#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:40:18 2019

@author: 278mt
"""

import re
import bibdoigetter as bdg
from os import sys

try:
    if sys.argv[1] in ["-v", "--version"]:
        print(bdg.__version__)
        exit()
    elif sys.argv[1] in ["-w", "--write"]:
        PATH = sys.argv[2]
        OUTPUT = sys.argv[2]
    elif sys.argv[1] in ["-o", "--output"]:
        PATH = sys.argv[2]
        OUTPUT = sys.argv[3]
    elif sys.argv[1] in ["-h", "--help"] or sys.argv[1][0] == "-":
        bdg.help()
        exit()
    else:
        PATH = sys.argv[1]
        DIR = re.search(".*/", PATH)
        if DIR is not None:
            OUTPUT = DIR.group(0) + "output.bib"
        else:
            OUTPUT = "output.bib"
except IndexError:
    PATH = input("bibファイルのパスを入力してください: ")
    OUTPUT = "output.bib"

bdg.splitarticles(PATH, OUTPUT)