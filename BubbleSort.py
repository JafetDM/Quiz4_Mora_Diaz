import time
import random

arreglo = [random.randint(0,100) for i in range(5000)]

def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


inicio = time.perf_counter()
# Sample list to be sorted


bubble_sort(arreglo)

print("BubbleSorted list time is:")

fin = time.perf_counter()

duracion = fin - inicio

print(duracion)
