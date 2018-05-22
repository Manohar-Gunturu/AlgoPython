arr = [0, 3, 1, 5, 2, 4, 6, 1, 3, 0]
# arr = [5, 2, 4, 6, 1, 3]


def merge(array, begin, mid, end):
    # size of first array [begin, mid]
    n1 = mid - begin + 1  # +1 as index starts at 0
    # size of first array [mid+1, end]
    n2 = end - mid
    # temp array to hold left and right
    leftarr = [0] * (n1)
    rightarr = [0] * (n2)

    for i2 in range(0, n1):
        leftarr[i2] = array[i2 + begin]

    for i1 in range(0, n2):
        rightarr[i1] = array[i1 + mid + 1]

    # leftarr[n1] = -1
    # rightarr[n2] = -1

    i = 0
    j = 0
    k = begin
    while i < n1 and j < n2:
        if leftarr[i] <= rightarr[j]:
            array[k] = leftarr[i]
            i = i + 1
        else:
            array[k] = rightarr[j]
            j = j + 1
        k = k + 1

    while i < n1:
        array[k] = leftarr[i]
        i = i + 1
        k = k + 1

    while j < n2:
        array[k] = rightarr[j]
        j = j + 1;
        k = k + 1;


def mergesort(array, l, r):
    if l < r:
        mid = round((l + (r - 1)) / 2)
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid, r)


mergesort(arr, 0, len(arr) - 1)

for i in range(0, len(arr)):
    print(arr[i])
