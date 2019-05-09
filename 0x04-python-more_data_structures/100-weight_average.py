#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(s * w for s, w in my_list) / sum(w for s, w in my_list)
