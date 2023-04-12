def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        arr[n//2:n] = sorted(arr[n//2:n])
        arr[0:n//2] = sorted(arr[0:n//2])
        count = 0
        finalCount = 0
        i = 0
        j = n//2
        flag = False
        while i < n//2:
            while j < n and arr[i] >= 5 * arr[j]:
                count += 1
                j += 1
                flag = True
            if flag:
                finalCount += count
            i += 1
        return finalCount