
import os
from os.path import join

SETTINGS_ROOT = os.path.dirname(__file__)
# b = SETTINGS_ROOT.split('/')

# c = '/'.join(b[:-1])
a = os.path.split(SETTINGS_ROOT)[0]

MEDIA = 'media' 
b = os.path.join(a,MEDIA)
print a
print b
# print c
# print os.path.join(b[1],b[2])