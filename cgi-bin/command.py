#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
command = form.getvalue('command')
print("Content-type:text/json\r\n\r\n")
print(command)
