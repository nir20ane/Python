class QuickSort(object):
    def sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi-1)
            self.sort(arr, pi+1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low -1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

qs = QuickSort()
arr = [19, 16, 12, 0, 4, 2, 1]
print(arr)
qs.sort(arr, 0, len(arr)-1)
print(arr)
