class MergeSort(object):
    def sort(self, arr, l, r):
        if l < r:
            m = l + (r-l)/2
            self.sort(arr, l, m)
            self.sort(arr, m+1, r)
            self.mergehalves(arr, l, m, r)


    def mergehalves(self, arr, l, m, r):
        n1 = m-l+1
        n2 = r-m
        L = []
        R = []
        for i in range(n1):
            L.append(arr[l+i])
        for j in range(n2):
            R.append(arr[m+1+j])
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

ms = MergeSort()
arr = [7, 8, 10, 12, 11, 4]
print(arr)
ms.sort(arr, 0, len(arr)-1)
print(arr)
