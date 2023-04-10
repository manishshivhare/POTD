def maxIntersections(self, lines, N):
        dict = {}
        for i in range(N):
            
            for j in range(lines[i][0], lines[i][1]+1):
                if j in dict:
                    dict[j]+=1
                else:
                    dict[j] =1
        return max(dict.values())
