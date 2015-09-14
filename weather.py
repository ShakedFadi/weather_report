# -*- coding: utf-8 -*-
__author__ = 'knedlus'


import urllib2
#import re
import time

response = urllib2.urlopen("http://www.siol.net/vreme.aspx")
returned_data = response.read()

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

needed_data = find_between(returned_data, 'id="weather"', 'class="news"')

city = find_between(needed_data, '<div class="cc"><span>', '</span></div>')
situation = find_between(needed_data, '<div class="cd">', '</div>')
degrees = find_between(needed_data, '<div class="ct">', '<sup>&deg;C</sup></div>')+"°C"
pressure = find_between(needed_data, '<p>Pritisk: <b>', '</b></p>')
humidity = find_between(needed_data, '<p>Vlaga: <b>', '</b></p>')
wind = find_between(needed_data, '<p>Veter: <b>', '</b></p>')

#print needed_data
print "*"*45
print """###### Vreme ######
Kraj: %s
Dan in ura: %s\n
Stanje: %s
Stopinje: %s
Pritisk: %s
Vlaga: %s
Veter: %s
""" %(city, time.strftime("%a, %d %b %Y %H:%M:%S") ,situation.capitalize(), degrees, pressure, humidity, wind)
print "*"*45

