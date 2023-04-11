def solve(self, a, b, c):
        #your code goes here
        max_n = max(a,max(b,c))
        if (max_n > 2 * (a+b+c+1 - max_n)):
            return -1
        return a+b+c