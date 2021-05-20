import time

def quicksort(arr, p, r):
  if p < r:
    q = partition(arr, p, r)
    quicksort(arr, p, q-1)
    quicksort(arr, q+1, r)
 

def partition(arr, p, r):
  x = arr[r]
  i = p - 1

  for j in range(p, r):
    if arr[j] <= x:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[r] = arr[r], arr[i+1]
  return i+1


arr = []
while(True):
  try:
    n = int(input())
    arr.append(n)
  except EOFError:
    break 

ini = time.time()
quicksort(arr, 0, len(arr)-1)
fim = time.time()
print("Tempo de execução:", fim-ini)
print(arr)