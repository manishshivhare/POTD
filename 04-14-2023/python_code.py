def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        st = [(color[0], radius[0])]
        for i in range(1, N):
            if st and st[-1][0] == color[i] and st[-1][1] == radius[i]:
                st.pop()
            else:
                st.append((color[i], radius[i]))
                
        return len(st)