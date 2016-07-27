#!/usr/bin/env python
import os
import sys

def bubbleSort(arr, size):
	sorted = False
	while not sorted:
		sorted = True;
		for i in xrange(1, size):
			if arr[i] < arr[i - 1]:
				arr[i], arr[i - 1] = arr[i - 1], arr[i]
				sorted = False;

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Too few arguments...\nUsage: python bubbleSort.py [file]\n"
	else:
		infile = open(sys.argv[1], "r")
		fname, fext = os.path.splitext(sys.argv[1])
		outfile = open(fname + "_out" + fext, "w")
		nums = map(lambda x: float(x) if x.find(".") != -1 else int(x), infile.read().split(","))
		bubbleSort(nums, len(nums))
		outfile.write(",".join(map(str, nums)))
		infile.close()
		outfile.close()
