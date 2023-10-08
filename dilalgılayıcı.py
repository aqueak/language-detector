# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:45:46 2023

@author: FURKAN
"""

import langid 
def detect_language(text):
    return langid.classify(text)[0]

text = input("Dil gir : ")
print(detect_language(text))