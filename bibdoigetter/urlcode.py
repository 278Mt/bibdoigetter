#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:22:49 2019

@author: 278mt
"""

CODE_TABLE = {" ": "%20","!": "%21","\"":"%22","#": "%23",\
              "$": "%24","%": "%25","&": "%26","\'":"%27",\
              "(": "%28",")": "%29","*": "%2A","+": "%2B",\
              ",": "%2C","/": "%2F",":": "%3A",";": "%3B",\
              "<": "%3C","=": "%3D",">": "%3E","?": "%3F",\
              "@": "%40","[": "%5B","]": "%5D","^": "%5E",\
              "`": "%60","{": "%7B","|": "%7C","}": "%7D",\
              "~": "%7E"}

def encode(string):
    for key in CODE_TABLE:
        string = string.replace(key, CODE_TABLE[key])
    return string

def decode(string):
    for key in CODE_TABLE:
        string = string.replace(CODE_TABLE[key], key)
    return string