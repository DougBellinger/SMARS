#!/usr/bin/python

import sys
sys.path.append(r'/usr/lib/cgi-bin')
import pydevd
pydevd.settrace('192.168.2.63') # replace IP with address
                                # of Eclipse host machine


i = 3
p = 'Hello!' * i
print p