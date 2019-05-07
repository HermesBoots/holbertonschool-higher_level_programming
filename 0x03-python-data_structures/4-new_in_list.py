#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	l = list(my_list)
	if idx >= 0 and idx <= len(l):
		l[idx] = element
	return l
