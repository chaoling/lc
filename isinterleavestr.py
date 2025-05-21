class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        brute force estimate: 2^n * 2^m, where n, m = len(s1), len(s2)
        dp[0][0] => True take 0 len str from s1 and 0 len str from s2 and can we make s3? yes! empty + empty == empty!
        dp[i][j] => if take [0:i] from s1 and[0:j] from s2, can we make s3[0:i+j]?
        if s1[i-1] == s3[i+j-1] and dp[i-1][j] then we can take from s1[i]
        if s2[j-1] == s3[i+j-1] and dp[i][j-1] then we can take from s2[j]
        check boundary conditions
        list table: rows: s1, cols: s2
        '''
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        dp =[[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True #empty + empty = empty!
        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        
        return dp[m][n]
if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(s.isInterleave("aabc", "abad", "aabadabc"))
    print(s.isInterleave("a", "", "a"))
    print(s.isInterleave("a", "b", "ab"))