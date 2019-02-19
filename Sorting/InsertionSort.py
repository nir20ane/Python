"""
In place sort:
O(n**2) time complexity, O(1) space
each item in array, we have n swap
so n items * n swaps = O(n**2)
"""
class InsertionSort(object):
    def insertionsort(self, arr):
        for i in range(1, len(arr)):
            j = i-1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = key

inst = InsertionSort()
arr = [10000, 34, 900000, 12, -8765444, 45223, 1234]
print(arr)
inst.insertionsort(arr)
print(arr)
