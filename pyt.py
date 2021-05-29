from random import shuffle

import resource, sys
from quicksort import quicksort
from mergesort import mergesort
from insertionsort import insertion
from bubblesort import bubble
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

arr = [x for x in range(1, 200001)]

# shuffle(arr)
print(arr[:30])
print()

print(len(arr))
bubble(arr)
# insertion(arr)

print(arr[200000-30:])