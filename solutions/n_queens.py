# Question number: 51
# Level: hard
# Author: Naama Tzadok
# Date: Dec 02, 2025 12:35

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        colls = set()
        n_diag = set()
        p_diag = set()

        board = [["." for _ in range(n)] for _ in range(n)]
        def solve(row):
            if row == n:
                sol = ["".join(r) for r in board]
                solutions.append(sol) # add to solutions
                return
            
            for i in range(n):
                if i in colls or row-i in p_diag or row+i in n_diag: 
                    continue
                
                board[row][i] = "Q"
                colls.add(i)
                p_diag.add(row-i)
                n_diag.add(row+i)

                solve(row+1)

                board[row][i] = "."
                colls.remove(i)
                p_diag.remove(row-i)
                n_diag.remove(row+i)
            
        solve(0)
        return solutions


# Time Complexity: O(n!)
# Space Complexity: O(n^2)