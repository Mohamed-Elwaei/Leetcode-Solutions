class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        order = []
        curr = ""
        n = [n]

        def dfs(curr = ""):
          if curr and int(curr) >= n[0]:
              return
          nums = "0123456789" if curr else "123456789"

          for c in nums:
              curr += c
              if int(curr) <= n[0]:
                order.append(int(curr))
              dfs(curr)
              curr = curr[:-1]
        dfs()
        return order
            
        