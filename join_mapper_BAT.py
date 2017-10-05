#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <TV Show type, value> input file
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
# --------------------------------------------------------------------------

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 
#    print ( '%s\t%s' % (key_in, value_in.isdigit() ) )
    #print key_in
    if value_in.isdigit() or value_in == 'BAT':           #if this entry has <date word> in key
        show_name = key_in      #now get date from key field
        value_out = value_in
        print( '%s\t%s' % (show_name, value_out) )  #print a string, tab, and string

