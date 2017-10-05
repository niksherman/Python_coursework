#! /usr/bin/env python
import sys

count_show_list = []
count_num_list = []
show_list = []

for line in sys.stdin:
	## Build 2 lists, one with the counts and one with ABC TV shows
	line = line.strip()
	key_value = line.split()
	 
	if ( key_value[1] == 'ABC' ):
		show_list.append(key_value[0])
#		print ( '%s' % (show_list[0]) )	

	if ( key_value[1].isdigit() ):
		count_show_list.append(key_value[0])
		count_num_list.append(key_value[1])
#		print ( '%s\t%s' % (count_show_list[0], count_num_list[0]))

len_count_list = len(count_show_list)
len_show_list = len(show_list)
abc_shows_count = []
abc_shows_name = []
show_count = 0
ABC_show = 0
for i in range(0, len_count_list):
	for j in range (0, len_show_list): 
		if (count_show_list[i] == show_list[j]): 
			ABC_show = 1
	if (ABC_show == 1): 

#		show_count = show_count + int(count_num_list[i])
		
#		print( 'Viewers by TV show %s\t%s' % (count_show_list[i], show_count))
		abc_shows_name.append(count_show_list[i])
		abc_shows_count.append(count_num_list[i])
		ABC_show = 0	
#		show_count = 0

show_used_up = []
len_abc_shows = len(abc_shows_name)
u = 0
prev_show = ''
rollup_sum = 0
grp_show_name = []
grp_show_count = []

for a in range(0, len_abc_shows):
		curr_show = abc_shows_name[a]
		if (curr_show not in show_used_up):
			show_used_up.append(curr_show)
			for b in range(a+1, len_abc_shows):
				if (curr_show == abc_shows_name[b]):
					rollup_sum = rollup_sum + int(abc_shows_count[b])
			grp_show_name.append(curr_show)
			grp_show_count.append(rollup_sum)
		rollup_sum = 0

tot_show_count = 0			
len_grped = len(grp_show_name)
for g in range(0, len_grped):
	print ( '%s\t%s' % (grp_show_name[g], grp_show_count[g]))
	tot_show_count = tot_show_count + int(grp_show_count[g])


# print ( 'total count %s' % (tot_show_count))

