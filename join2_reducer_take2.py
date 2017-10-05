#! /usr/bin/env python
import sys

running_tot=0
prev_key=''
show_name=''
abc_found=0

for line in sys.stdin:
	line = line.strip()
	key_value = line.split('\t')

	curr_key=key_value[0]
	curr_val=key_value[1]
	
#	print ( 'prev_key %s\t curr_key %s\t abc_found %s running_tot %s' % (prev_key,curr_key,abc_found,running_tot))

	if (prev_key != '') and (prev_key != curr_key):  
		if (abc_found==1):
			print ( '%s\t%s' % (show_name,running_tot))
			running_tot=int(curr_val)
			prev_key=curr_key
		else: 
			running_tot=int(curr_val)
			prev_key=curr_key
	elif (prev_key == curr_key) and (curr_val=='ABC'):
		abc_found=1
	else:
		abc_found=0
		running_tot = running_tot + int(curr_val)
		show_name=curr_key
		prev_key=curr_key
#		print ('%s\t%s' % (show_name,running_tot))
