def sample(A, B, C, D, E, F, G, H):
    rect1 = abs(C - A) * abs(B - D)
    rect2 = abs(E - G) * abs(F - H)
    w = min(C, G) - max(A, E)
    h = min(D, H) - max(B, F)
    if w <= 0 or h <= 0:
        return rect1 + rect2
    return rect1 + rect2 - w * h


def sample2(A, B, C, D, E, F, G, H):
    area1 = (C - A) * (D - B)

    area2 = (G - E) * (H - F)
    if E > C or G < A or F > D or H < B:
        return area1 + area2
    else:
        return -((min(D, H) - max(B, F)) * (min(C, G) - max(E, A))) + area1 + area2


class Solution:

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        print(A, B, C, D, E, F, G, H)
        # area of triangle 1 & 2
        area_triangle1 = (A - C) * (B - D)
        area_triangle2 = (E - G) * (F - H)

        # find the intersection
        area_intersection = 0
        area_intersection = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        """
        if not(E > C or G < A or F > D or B > H):
            area_intersection = abs( (max(A , E) - min(C, G) ) * ( max(B, F) - min(D, H) ) )

        """
        return area_triangle1 + area_triangle2 - area_intersection


s = Solution()
s.computeArea(3, 3, 4, 4, -2, -2, 2, 2)
