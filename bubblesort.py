def bubble(arr):
  cont = 0
  for i in range(len(arr)):
    for j in range(len(arr)-1, i, -1):
      if arr[j] < arr[j-1]:
        cont += 1
        aux = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = aux
  return cont

