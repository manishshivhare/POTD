def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        count = -1
        mp = {}
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = count
            else:
                count = max(count, mp[arr[i]] + time[arr[i]-1])
                mp[arr[i]] = count
            count += 1
        return count
            