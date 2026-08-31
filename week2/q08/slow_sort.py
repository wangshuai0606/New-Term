import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

if __name__ == '__main__':
    import random
    data = [random.randint(1, 1000) for _ in range(5000)]
    
    start = time.time()
    sorted_data = bubble_sort(data[:])
    print(f"Bubble sort: {time.time() - start:.3f}s")
    
    start = time.time()
    dups = find_duplicates(data[:])
    print(f"Find duplicates: {time.time() - start:.3f}s")