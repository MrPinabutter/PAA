import time

def heapsort():
  pass

arr = []
while(True):
  try:
    n = int(input())
    arr.append(n)
  except EOFError:
    break 

ini = time.time()
heapsort(arr, 0, len(arr)-1)
fim = time.time()
print("Tempo de execução:", fim-ini)
print(arr)