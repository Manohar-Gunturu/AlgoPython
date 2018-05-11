# selection sort and insertion sort difference is well explained at
# https://stackoverflow.com/a/15799095/2717984

# Insertion sort worse case always applies to selection sort, because
# Insertion sort is better than selection sort, as you can see the nested loop in
# insertion sort stops wherever it finds grater number than key, but in selection sort
# we always have to check the complete chunk of array ahead of current position to find minimum

arr = [5, 2, 4, 6, 1, 3]
length = len(arr)

for i in range(0, length):  # n times
    minimal = i             # n - 1 times
    for j in range(i, length):   # sigma n to 0 times
        if arr[j] < arr[minimal]:  # sigma n to 0 times
            minimal = j            # sigma n to 0 times
    arr[minimal], arr[i] = arr[i], arr[minimal]   # sigma n to 0 times

for j in range(0, len(arr)):
    print(arr[j])
