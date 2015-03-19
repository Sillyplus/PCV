#!/usr/bin/env python
# coding=utf-8

import os
from PIL import Image

path = '../data/'
flist = [os.path.join(path, f) for f in os.listdir(path)]

print flist
