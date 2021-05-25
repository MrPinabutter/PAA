def mergesort(arr, p, u):
  cont = 0
  if p < u:
    cont += 1
    q = int((p+u)/2)

    cont += mergesort(arr, p, q)
    cont += mergesort(arr, q+1, u)
    cont += merge(arr, p, q, u)
  return cont

def merge(arr, p, q, u):
  n1 = q-p+1
  n2 = u-q
  l = []
  r = []

  for i in range(n1):
    l.append(arr[p+i])
  for j in range(n2):
    r.append(arr[q+j+1])

  l.append(float('inf'))
  r.append(float('inf'))
  i = 0
  j = 0
  cont = 0
  for k in range(p, u+1):
    cont += 1
    if l[i] <= r[j]:
      arr[k] = l[i]
      i += 1
    else:
      arr[k] = r[j]
      j += 1
  return cont
