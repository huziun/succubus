def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smalles_index = i
            print(smallest_index)
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        #arr.pop(smallest)
        #newArr.append(smallest)
        newArr.append(arr.pop(smallest))
        print(newArr)
    return newArr

#my_arr = [1,3,2,9,-2,0]
print(selectionSort([3,2,9]))
