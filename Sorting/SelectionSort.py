"""
In place sort:
O(n**2) time complexity, O(1) space
pic the smallest everytime and move it to front of list
so n items * n swaps = O(n**2)
"""
class SelectionSort(object):
    def selectionsort(self, arr):
        n = len(arr)
        for i in range(0, n-1):
            minindex = i
            for j in range(i+1, n):
                if arr[j] < arr[minindex]:
                    minindex = j
            arr[minindex], arr[i] = arr[i], arr[minindex]


ssort = SelectionSort()
arr = [10000, 34, 900000, 12, -8765444, 45223, 1234]
print(arr)
ssort.selectionsort(arr)
print(arr)
