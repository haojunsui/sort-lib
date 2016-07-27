#!/usr/bin/env python
import os
import sys

def insertSort(arr, size):
	newValue = pos = -1

	for newPos in xrange(1, size):
		newValue = arr[newPos]
		pos = newPos
		while pos > 0 and newValue < arr[pos - 1]:
			arr[pos] = arr[pos - 1]
			pos -= 1
		arr[pos] = newValue

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Too few arguments...\nUsage: python insertSort.py [file]\n"
	else:
		infile = open(sys.argv[1], "r")
		fname, fext = os.path.splitext(sys.argv[1])
		outfile = open(fname + "_out" + fext, "w")
		nums = map(lambda x: float(x) if x.find(".") != -1 else int(x), infile.read().split(","))
		insertSort(nums, len(nums))
		outfile.write(",".join(map(str, nums)))
		infile.close()
		outfile.close()
