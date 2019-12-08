arr1 = [2, 6, 8, 9, 11, 13, 17]
arr2 = [3, 6, 7, 8, 10, 13]
arr3 = [4, 5, 6, 8, 9, 11, 13]

arr_container = {0: arr1, 1: arr2, 2: arr3}
tracker = [0, 0, 0]
intersection = []
flag = True
while flag:

    max_elem = arr_container[0][tracker[0]]

    for t in range(0, len(tracker)):
        max_elem = max(max_elem, arr_container[t][tracker[t]])

    common_element = arr_container[0][tracker[0]]
    is_common = True
    for t in range(0, len(tracker)):
        if common_element != arr_container[t][tracker[t]]:
            is_common = False

    if is_common:
        intersection.append(common_element)
        for t in range(0, len(tracker)):
            tracker[t] += 1
    else:
        for t in range(0, len(tracker)):
            if arr_container[t][tracker[t]] < max_elem:
                tracker[t] += 1

    print(max_elem, arr_container, tracker, intersection)

    for t in range(0, len(tracker)):
        if tracker[t] >= len(arr_container[t]):
            flag = False



