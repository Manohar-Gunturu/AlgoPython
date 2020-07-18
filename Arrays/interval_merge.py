import bisect
from typing import List, Tuple


def schedule(old: List[Tuple[int, int]], new: List[Tuple[int, int]]) -> List[bool]:
    """
    >>> schedule([], [(18, 7), (12, 10)])
    [True, True]

    >>> schedule([(10, 5), (25, 15)], [(18, 7), (12, 10)])
    [True, False]

    >>> schedule([(10, 1000)], [(18, 7), (12, 10)])
    [False, False]

    >>> schedule([(1,1), (3,1)], [(2,1), (4,1)])
    [True, True]
    """

    ooo: List[int] = []

    for s, t in old:
        ooo.append(s)
        ooo.append(s + t)

    ooo.sort()

    ret = []
    for s, t in new:
        i = bisect.bisect(ooo, s)
        if i & 1:
            ret.append(False)
        else:
            j = bisect.bisect_left(ooo, s + t)
            if j == i:
                ret.append(True)
            else:
                ret.append(False)
    return ret


schedule([(10, 5), (25, 15)], [(1, 7), (12, 10)])