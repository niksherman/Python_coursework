#! /usr/bin/env python

## Mapper code to input a line of text and output <word, 1>

import sys 

for line in sys.stdin:
	line = line.strip() ## takes out the carriage return
	keys = line.split() ## uses blank as a delimiter and splits the line into segments
  
	for key in keys:
		value = 1
		print('{0}\t{1}'.format(key,value)) 
