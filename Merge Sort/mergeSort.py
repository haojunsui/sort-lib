#!/usr/bin/env python
import os
import sys

def mergeSort(arr, size):
	if size > 1:
		halfSize = size / 2
		otherHalf = size - halfSize
		listA = arr[:halfSize]
		listB = arr[halfSize:]

		mergeSort(listA, halfSize)
		mergeSort(listB, otherHalf)

		i = j = k = 0
		while i < halfSize and j < otherHalf:
			if listA[i] < listB[j]:
				arr[k] = listA[i]
				i += 1
			else:
				arr[k] = listB[j]
				j += 1
			k += 1

		while i < halfSize:
			arr[k] = listA[i]
			i += 1
			k += 1

		while j < otherHalf:
			arr[k] = listB[j]
			j += 1
			k += 1

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Too few arguments...\nUsage: python mergeSort.py [file]\n"
	else:
		infile = open(sys.argv[1], "r")
		fname, fext = os.path.splitext(sys.argv[1])
		outfile = open(fname + "_out" + fext, "w")
		nums = map(lambda x: float(x) if x.find(".") != -1 else int(x), infile.read().split(","))
		mergeSort(nums, len(nums))
		outfile.write(",".join(map(str, nums)))
		infile.close()
		outfile.close()
