def find_split(self, a):
        n = len(a)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i] = a[i]
            if i > 0:
                prefix_sum[i] += prefix_sum[i - 1]
        split_points = [[0, 0]]
        for i in range(1, n):
            low, high = 1, i
            min_diff = 2e18
            split = [0, 0]
            while low <= high:
                mid = (low + high) // 2
                x = prefix_sum[mid - 1]
                y = prefix_sum[i] - x
                if abs(x - y) < min_diff:
                    min_diff = abs(x - y)
                    split[0] = x
                    split[1] = y
                if x > y:
                    high = mid - 1
                else:
                    low = mid + 1
            split_points.append(split)
        return split_points

    def minDifference(self, N, A): 
        ans = 2e18
        x = self.find_split(A)
        y = self.find_split(A[::-1])[::-1]  # Reverse A and find split, then reverse back
        for i in range(1, N - 2):
            ans = min(ans, max(max(x[i][0], x[i][1]), max(y[i + 1][0], y[i + 1][1])) - min(
                min(x[i][0], x[i][1]), min(y[i + 1][0], y[i + 1][1])))
        return ans