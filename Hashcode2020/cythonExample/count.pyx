from libc.stdlib cimport malloc
from cpython.mem cimport PyMem_Malloc
def arr():
	cdef double *array= <double*>PyMem_Malloc(10000*sizeof(double))
	cdef i=0
	while(i<10000):
		array[i]=i
		i+=1



cpdef void countUp(int n):
	cdef int i=0
	while(i<n):
		i+=1

