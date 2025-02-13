'''question 3'''



class SortKarde:
    def __init__(self, arr):
        self.arr = arr

    def selectionwala(self):
        n = len(self.arr)
        for i in range(n - 1):
            lowterm = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[lowterm]:
                    lowterm = j

            temp = self.arr[i]
            self.arr[i] = self.arr[lowterm]
            self.arr[lowterm] = temp

    def returnthe_sortedlist(self):
        return self.arr


class BinarySearchKarde:
    def __init__(self, arr):
        self.arr = arr

    def searcher(self, target):
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


a = int(input("How many strings you want to enter? "))
arr = [input("Enter a string: ") for _ in range(a)]

sorter = SortKarde(arr)
sorter.selectionwala()
sorted_list = sorter.returnthe_sortedlist()
print("Sorted list:", sorted_list)

target = input("Enter the string to search: ")

searcher = BinarySearchKarde(sorted_list)
result = searcher.searcher(target)

if result != -1:
    print(f"String found at index {result}")
else:
    print("String not found")
