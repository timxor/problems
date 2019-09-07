class Solution(object):
    def largestTriangleArea(self, points):

        # helper function
        def area(p, q, r):
            #shoelace formula: .5 * abs
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))
