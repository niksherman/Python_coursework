#! /usr/bin/env python
import sys

prev_word		= " "
months			= ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dates_to_output		= []
day_cnts_to_output	= []
lines			= 0

for line in sys.stdin:
	line		= line.strip()
	key_value	= line.split('\t')
	line_cnt	= line_cnt+1

	curr_word	= key_value[0]
	value_in	= key_value[1]

	if curr_word != prev_word:
		  if line_cnt>1:
		for i in range(len(dates_to_output)):
		dates_to_output	=[]
			day_cnts_to_output=[]
		  prev_word	= curr_word

	if (value_in[0:3] in months):
	else:

for i in range(len(dates_to_output)):
	print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))

