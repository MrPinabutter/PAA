def insertion(arr):
  cont = 0
  for j in range(1, len(arr)):
    chave = arr[j]
    i = j-1
    while i >= 0 and arr[i] > chave:
      cont += 1
      arr[i+1] = arr[i]
      i -= 1
    arr[i+1] = chave
  return cont
    
