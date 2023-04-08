
def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        st = []
        for n in arr:
            if not st:
                st.append(n)
                continue
            
            if (st[-1] < 0) != (n < 0):
                st.pop()
            else:
                st.append(n)
            
        ans = []
        while st:
            ans.append(st.pop())
        ans.reverse()
        return ans