class HeapSort(object):
    def sorts(self, arr):
        n = len(arr)

        for i in range(n-1/2, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, -1, -1):
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            self.heapify(arr, i, 0)

    def heapify(self, arr, n, i):
        largest = i
        l = i*2 + 1
        r = i*2 + 2
        if l<n and arr[l] > arr[largest]:  # important
            largest = l
        if r<n and arr[r] > arr[largest]:  # important
            largest = r
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)


hp = HeapSort()
arr = [11, 13, 12, 5, 7, 6]
print(arr)
hp.sorts(arr)
print(arr)
