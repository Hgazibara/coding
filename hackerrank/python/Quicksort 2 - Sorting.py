import sys

def print_array(arr):
	if len(arr) <= 1: return
	for x in arr: print('{} '.format(x),end='')
	print()

def choose_pivot(arr):
	return arr[0]

def swap(arr, x, y):
	tmp = arr[y]
	arr[y] = arr[x]
	arr[x] = tmp
	
def sort(arr):
	if len(arr) <= 1: return arr
	p = choose_pivot(arr)
	(A,B) = partition(arr, p)
	C = sort(A)
	D = sort(B)
	print_array(C+[p]+D)
	return C+[p]+D

def partition(arr, p):
	
	left = []
	right = []
	
	for x in arr:
		if x == p: continue
		if x < p: left.append(x)
		else: right.append(x)
	
	return (left,right)
	
# read input
input = [int(x) for x in sys.stdin.readlines()[1].split()]
sort(input)