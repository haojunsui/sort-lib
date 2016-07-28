#!/usr/bin/env python
import os
import sys

def quickSort(arr, size):
	if size <= 1:
		return arr
	pivot = arr[size / 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quickSort(left, len(left)) + middle + quickSort(right, len(right))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Too few arguments...\nUsage: python mergeSort.py [file]\n"
	else:
		infile = open(sys.argv[1], "r")
		fname, fext = os.path.splitext(sys.argv[1])
		outfile = open(fname + "_out" + fext, "w")
		nums = map(lambda x: float(x) if x.find(".") != -1 else int(x), infile.read().split(","))
		nums = quickSort(nums, len(nums))
		outfile.write(",".join(map(str, nums)))
		infile.close()
		outfile.close()
