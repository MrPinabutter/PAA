import time

def insertion(arr):
  for j in range(1, len(arr)):
    chave = arr[j]
    i = j-1
    while i >= 0 and arr[i] > chave:
      arr[i+1] = arr[i]
      i -= 1
    arr[i+1] = chave
    

arr = []
while(True):
  try:
    n = int(input())
    arr.append(n)
  except EOFError:
    break 

ini = time.time()
insertion(arr)
fim = time.time()
print("Tempo de execução:", fim-ini)
print(arr)