import sys
import random
import math
import numpy as np


class Packer:
    def __init__(self, fout, size, eps):
        self._fout = fout
        self._out_file = sys.stdout
        self._size = size
        self._eps = eps
        self._arr = []
		self._arr_ids = range(size)
        self._buckets = []
		self._buckets_weight = []
        self._buckets_count = 0

    # generates array of a[i] from (0, 1) interval
    def _gen_arr(self):
        i = 0
        while i < self._size:
            self._arr.append(random.random())
            i += 1

    # prints array to file
    def _print_arr(self, arr):
        i = 0
        while i < len(arr):
            self._out_file.write(arr[i])
            i += 1
	
	# prints summary
	def _print_results(self):
		self._out_file.write("Original array:")
		self._print_arr(self.arr)
		self._out_file.write("=========||=========")
		self._out_file.write("Total buckets number:")
		self._out_file.write(self._buckets_count)
		self._out_file.write("=========||=========")
		self._out_file.write("buckets:")
		i = 0;
		for bucket in self._buckets:
			self._out_file.write("bucket weight: ", self._bucket_weight[i])
			i += 1
			self._print_arr(bucket)

    def _k_pack(self, arr):
        pass

    def _first_fit(self, arr):
        for i in range(len(arr)):
        	flag = True
			for j in range(self._buckets_count)
				if arr[i] <= 1-self._buckets_weight[j]:
					self._buckets[j].append(arr[i])
					self._buckets_weight[j] += arr[i]
					flag = False
					break
			if flag == True:
				self._buckets.append([])
				self._buckets[self._buckets_count].append(arr[i])
				self._buckets_weight.append(arr[i])
				self._buckets_count += 1
				

    # runs algorithm
    def run(self):
        random.seed()
        if self._fout != '':
            self._out_file = open(self._fout, "w")
        self._gen_arr()

        # step 1, separate values < eps and the other ones
        less_eps = []
        more_eps = []
        i = 0
        while i < self._size:
            if self._arr[i] < self._eps:
                less_eps.append(self._arr[i])
            else:
                more_eps.append(self._arr[i])
            i += 1

        # step 2, sort other elements
        more_eps.sort()

        # step3, split them to K groups
        k = math.ceil(1 / self._eps ** 2)
        chunks = []
        if k > len(more_eps):
            i = 0
            while i < len(more_eps):
                chunks.append([more_eps[i]])
                i += 1
        else:
            chunk_len = len(more_eps) / k
            i = 0
            while i < len(more_eps):
                j = 0
                chunk = []
                while j < chunk_len and i < len(more_eps):
                    chunk.append(more_eps[i])
                    j += 1
                    i += 1
                chunks.append(chunk)

        # step 4, ceil the weight to max_weight in each group
        new_chunks = chunks
        for new_chunk in new_chunks:
            max_weight = max(new_chunk)
            new_chunk = (new_chunk * 0) + max_weight

        # step 5, pack these elements
        self._k_pack(new_chunks)





