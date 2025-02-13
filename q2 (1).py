'''question 2 '''


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


a = int(input("How many strings you want to enter? "))
arr = []

for i in range(a):
    stri = input("Enter your strings: ")
    arr.append(stri)

sorter = SortKarde(arr)
sorter.selectionwala()

print("The sorted strings are:", sorter.returnthe_sortedlist())