#!/usr/bin/env python
import os
import sys

def selectSort(arr, size):
	minPos = -1;
	for sorted in xrange(size):
		minPos = sorted
		for next in xrange(sorted + 1, size):
			if arr[minPos] > arr[next]:
				minPos = next
		arr[sorted], arr[minPos] = arr[minPos], arr[sorted]

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Too few arguments...\nUsage: python selectSort.py [file]\n"
	else:
		infile = open(sys.argv[1], "r")
		fname, fext = os.path.splitext(sys.argv[1])
		outfile = open(fname + "_out" + fext, "w")
		nums = map(lambda x: float(x) if x.find(".") != -1 else int(x), infile.read().split(","))
		selectSort(nums, len(nums))
		outfile.write(",".join(map(str, nums)))
		infile.close()
		outfile.close()
