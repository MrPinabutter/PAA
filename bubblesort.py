def bubble(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1, i, -1):
      if arr[j] < arr[j-1]:
        aux = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = aux
  

