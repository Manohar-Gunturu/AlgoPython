def partition(a, low, high):

    pivot = a[high]

    pivot_location = low - 1

    for j in range(low, high):

        if a[j] < pivot:
            pivot_location = pivot_location + 1
            a[pivot_location], a[j] = a[j], a[pivot_location]

    a[pivot_location + 1], a[high] = a[high], a[pivot_location + 1]

    return pivot_location + 1


def quickSort(a, low, high):
    if low < high:
        pivot_location = partition(a, low, high)
        quickSort(a, low, pivot_location - 1)
        quickSort(a, pivot_location + 1, high)


def kthLargest():
    a = [10, 80, 30, 90, 40, 50, 70]
    k = 5
    low = 0
    high = len(a) - 1
    while True:

        pivot_location = partition(a, low, high)
        if pivot_location == k:
            return a[pivot_location]
        if pivot_location > k:
            low = low
            high = pivot_location - 1
        else:
            low = pivot_location + 1
            high = len(a) - 1


# result = kthLargest()
# print(result)

a = [5, 0, 1, -1, 5]
quickSort(a, 0, len(a) - 1)
print(a)
