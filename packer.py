import sys
import random
import math


class Packer:
    def __init__(self, fout, len, eps):
        self._fout = fout
        self._out_file = sys.stdout
        self._size = len
        self._eps = eps
        self._arr = []
        self._buckets = []
        self._buckets_count = 0

    # generates array of a[i] from (0, 1) interval
    def _gen_arr(self):
        i = 0
        while i < self._size:
            self._arr.append(random.random())
            i += 1

    # prints array to file
    def _print_arr(self):
        i = 0
        while i < self._size:
            self._out_file.write(self._arr[i])
            i += 1

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

        # step 2, sort other elements and split them to K groups
        more_eps.sort()
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
                chunks.append([more_eps[i]])
                i += 1

        # step 3,



