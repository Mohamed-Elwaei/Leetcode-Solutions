class Solution:
    def knightDialer(self, n: int) -> int:
        phone = ["123",
                 "456",
                 "789",
                 "*0*"]
        graph = {str(n):set() for n in range(10)}
        moves = lambda r,c:[(r-1,c-2),(r-2,c-1),(r-2,c+1),(r-1,c+2),(r+1,c+2),(r+2,c+1),(r+2,c-1),(r+1,c-2)]
        for r in range(len(phone)):
            for c in range(3):
                if phone[r][c] == '*':
                    continue
                for nr,nc in moves(r,c):
                    if 0<=nr<len(phone) and 0<=nc<len(phone[0]) and phone[nr][nc]!='*':
                        
                        key,value = phone[r][c],phone[nr][nc]

                        graph[key].add(value)
        
        matrix = []
        for _ in range(n+1):
            matrix.append([0] * 10)
        matrix [1] = [1] * 10
        for r in range(2,n+1):
            for c in range(10):
                for neigh in graph[str(c)]:
                    matrix[r][c] =( matrix[r][c] + matrix[r-1][int(neigh)]) % (10**9 + 7)

        return sum(matrix[-1]) % (10**9 + 7)
            