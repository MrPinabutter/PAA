import time

def bubble(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1, i, -1):
      if arr[j] < arr[j-1]:
        aux = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = aux

arr = []
while(True):
  try:
    n = int(input())
    arr.append(n)
  except EOFError:
    break 

ini = time.time()
bubble(arr)
fim = time.time()
print("Tempo de execução:", fim-ini)
print(arr)