#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
from URL_Lookup.URL_Lookup import URL_Lookup

"""
CGI flag for debugging purpose
True = execute python through html
False = execute python directly
"""
CGI = True
MalwareURL = True

"""
CGI stuff to connect from HTML
"""
cgitb.enable()
print "Content-Type: text/plain;charset=utf-8"
print
form = cgi.FieldStorage()

if CGI:
    URL = form["Field"].value
else:
    URL = "bolo100.com"

LookupInst = URL_Lookup(URL)

try:
    MalwareURL = LookupInst.lookup()
except:
    print "lookup Error"
    raise

if MalwareURL:
    print "URL is Malware (Not safe)"
else:
    print "URL is Safe"