import time
from mergesort import mergesort
from bubblesort import bubble
from heapsort import Heap
from quicksort import quicksort
from insertionsort import insertion

print("Escolha o algoritmo de ordenação desejado:")
print("0 - MergeSort")
print("1 - BubbleSort")
print("2 - HeapSort")
print("3 - QuickSort")
print("4 - InsertionSort")
n = int(input())

arrAle = []
arrDec = []
arrCres = []

f = open('500aleatorio.txt', 'r')
for line in f:
  arrAle.append(int(line))
f.close()

f = open('500decrescente.txt', 'r')
for line in f:
  arrDec.append(int(line))
f.close()

f = open('500crescente.txt', 'r')
for line in f:
  arrCres.append(int(line))
f.close()

times = []
if n == 0:  ### MERGE SORT 
  print("MergeSort aleatório")    ## ALEATORIO
  for i in range(3):
    ini = time.time()
    mergesort(arrAle.copy(), 0, len(arrAle)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print()
  print("MergeSort decrescente")  ## DECRESCENTE
  for i in range(3):
    ini = time.time()
    mergesort(arrDec.copy(), 0, len(arrDec)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )
  times = []
  print()
  print("MergeSort crescente")  ## CRESCENTE
  for i in range(3):
    ini = time.time()
    mergesort(arrCres.copy(), 0, len(arrCres)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )

elif n == 1:  ### QUICKSORT
  print("BubbleSort aleatório") ## ALEATORIO
  for i in range(3):
    ini = time.time()
    bubble(arrAle.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print()
  print("BubbleSort decrescente") ## DECRESCENTE
  for i in range(3):
    ini = time.time()
    bubble(arrDec.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )
  times = []
  print()
  print("BubbleSort crescente") ## CRESCENTE
  for i in range(3):
    ini = time.time()
    bubble(arrCres.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )

elif n == 2:  ### HEAPSORT
  print("HeapSort aleatório") ## ALEATORIO
  for i in range(3):
    ini = time.time()
    heap = Heap()
    heap.sort(a = arrAle.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print()
  print("HeapSort decrescente") ## DECRESCENTE
  for i in range(3):
    ini = time.time()
    heap = Heap()
    heap.sort(a = arrDec.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )
  times = []
  print()
  print("HeapSort crescente") ## CRESCENTE
  for i in range(3):
    ini = time.time()
    heap = Heap()
    heap.sort(a = arrCres.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )

elif n == 3:  ### QUICKSORT
  print("QuickSort aleatório") ## ALEATORIO
  for i in range(3):
    ini = time.time()
    quicksort(arrAle.copy(), 0, len(arrAle)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print()
  print("QuickSort decrescente") ## DECRESCENTE
  for i in range(3):
    ini = time.time()
    quicksort(arrDec.copy(), 0, len(arrDec)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )
  times = []
  print()
  print("QuickSort crescente") ## CRESCENTE
  for i in range(3):
    ini = time.time()
    quicksort(arrCres.copy(), 0, len(arrCres)-1)
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )

elif n == 4:  ### InsertionSort
  print("InsertionSort aleatório") ## ALEATORIO
  for i in range(3):
    ini = time.time()
    insertion(arrAle.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}')
  times = []
  print()
  print("InsertionSort decrescente") ## DECRESCENTE
  for i in range(3):
    ini = time.time()
    insertion(arrDec.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )
  times = []
  print()
  print("InsertionSort crescente") ## CRESCENTE
  for i in range(3):
    ini = time.time()
    insertion(arrCres.copy())
    fim = time.time()
    times.append(fim-ini)
  print("Tempos de execução: ", f'{times[0]:.5f}', f'{times[1]:.5f}', f'{times[2]:.5f}')
  print("Tempo de execução média:", f'{(times[0] + times[1] + times[2])/3:.5f}' )

