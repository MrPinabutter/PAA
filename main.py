import time
import resource, sys
from random import shuffle
from mergesort import mergesort
from bubblesort import bubble
from heapsort import Heap
from quicksort import quicksort
from insertionsort import insertion
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def render(title, func, params):
  times = []
  arr = params[0].copy()
  params.pop(0)
  print(title) ## ALEATORIO
  for _ in range(3):
    ini = time.time()
    func(arr.copy(), *params)
    fim = time.time()
    times.append(fim-ini)
  print()
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print("-"*40)

print("Escolha o algoritmo de ordenação desejado:")
print("0 - MergeSort")
print("1 - BubbleSort")
print("2 - HeapSort")
print("3 - QuickSort")
print("4 - InsertionSort")
n = int(input())

print("Número do tamanho de teste:")
print("0 - 100")
print("1 - 1000")
print("2 - 5000")
print("3 - 30000")
print("4 - 50000")
print("5 - 100000")
print("6 - 150000")
print("7 - 200000")
m = int(input())

if m == 0:
  c = 100
elif m == 1: 
  c = 1000
elif m == 2: 
  c = 5000
elif m == 3: 
  c = 30000
elif m == 4: 
  c = 50000
elif m == 5: 
  c = 100000
elif m == 6: 
  c = 150000
elif m == 7: 
  c = 200000

arr = [x for x in range(c)]

arrDec = arr[::-1].copy()
arrCres = arr.copy()
shuffle(arr)
arrAle = arr.copy()

times = []
if n == 0:  ### MERGESORT
  render("MergeSort aleatório", mergesort, [arrAle, 0, len(arrAle)-1])
  render("MergeSort decrescente", mergesort, [arrDec, 0, len(arrDec)-1])
  render("MergeSort crescente", mergesort, [arrCres, 0, len(arrCres)-1])

elif n == 1:  ### BUBBLESORT
  render("BubbleSort aleatório", bubble, [arrAle])
  render("BubbleSort decrescente", bubble, [arrDec])
  render("BubbleSort crescente", bubble, [arrCres])

elif n == 2:  ### HEAPSORT
  heap = Heap()
  render("HeapSort aleatório", heap.sort, [arrAle])
  render("HeapSort decrescente", heap.sort, [arrDec])
  render("HeapSort crescente", heap.sort, [arrCres])

elif n == 3:  ### QUICKSORT
  render("QuickSort aleatório", quicksort, [arrAle, 0, len(arrAle)-1])
  render("QuickSort decrescente", quicksort, [arrDec, 0, len(arrDec)-1])
  render("QuickSort crescente", quicksort, [arrCres, 0, len(arrCres)-1])

elif n == 4:  ### INSERSIONSORT
  render("InsertionSort aleatório", insertion, [arrAle])
  render("InsertionSort decrescente", insertion, [arrDec])
  render("InsertionSort crescente", insertion, [arrCres])
