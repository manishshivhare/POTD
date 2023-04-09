class Solution:
    def bestNumbers(self, N : int, A : int, B : int, C : int, D : int) -> int:
        # code here
        
        MOD = 10**9+7
        def _satisfy(v):
            while v:
                v, r = divmod(v, 10)
                if not(r==C or r==D): return False
            return True
        def _fact(n):
            ans, tmp = [1]*(n+1), 1
            for i in range(2, n+1):
                tmp = (tmp*i) % MOD
                ans[i] = tmp
            return ans
            
        # if A==B: return 1 if _satisfy(N*A) else 0
        ans = 0
        facts = _fact(N)
        for acnt in range(N+1):
            bcnt = N-acnt
            dsum = A*acnt + B*bcnt
            if not _satisfy(dsum): continue
            down = (facts[acnt] * facts[bcnt]) % MOD
            inv = pow(down, MOD-2, MOD)
            ans = (ans + facts[N] * inv) % MOD
        return ans

# The function first defines a constant MOD equal to 10^9 + 7, which is a prime number commonly used in modular arithmetic.

# The function then defines two helper functions: _satisfy and _fact. _satisfy takes an integer argument v and returns True if and only if all the digits of v are either C or D. _fact takes an integer argument n and returns a list of integers ans such that ans[i] is equal to i! modulo MOD for each i between 0 and n.

# The function then initializes a variable ans to 0 and computes the factorials of the numbers from 0 to N using the _fact function.

# The function then loops over all possible values of acnt between 0 and N, and for each value of acnt, computes the corresponding value of bcnt as N - acnt. It then computes the sum of digits dsum for all integers that have acnt digits equal to C or D and bcnt digits equal to C or D. If dsum does not satisfy the condition specified by A and B, the loop skips to the next value of acnt. Otherwise, the function computes the number of ways to choose acnt digits equal to C or D out of N total digits, and multiplies this by the number of ways to choose bcnt digits equal to C or D out of the remaining N - acnt digits. This gives the total number of integers that have acnt digits equal to C or D and bcnt digits equal to C or D. The function then adds this to ans.

# Finally, the function returns ans modulo MOD.