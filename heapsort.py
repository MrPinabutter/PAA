import time

class Heap:
    def heapify(self, a = [], n = 0, i = 0):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] > a [largest]:
            largest = l

        if r < n and a[r] > a[largest]:
            largest = r

        if largest != i:
            a[i], a[largest] = a[largest], a[i]

            self.heapify(a, n, largest)

    def sort(self, a):
        n = len(a)

        for i in range(int(n/2 - 1), -1, -1):
            self.heapify(a, n, i)

        for i in range(n - 1, -1, -1):
            a[0], a[i] = a[i], a[0]

            self.heapify(a, i, 0)



arr = []
while(True):
  try:
    n = int(input())
    arr.append(n)
  except EOFError:
    break 

ini = time.time()
heap = Heap()
heap.sort(a = arr)
fim = time.time()
print("Tempo de execução:", fim-ini)
print(arr)