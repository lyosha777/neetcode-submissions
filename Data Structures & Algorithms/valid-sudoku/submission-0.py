class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            seen = set()
            for j in range(n):
                curr = board[i][j]
                if curr in seen:
                    return False
                elif curr != ".":
                    seen.add(curr)

        for i in range(n):
            seen = set()
            for j in range(n):
                curr = board[j][i]
                if curr in seen:
                    return False
                elif curr != '.':
                    seen.add(curr)

        starts = [(0,0),(0,3),(0,6),
                (3,0),(3,0),(3,0),
                (6,0),(6,0),(6,0)]

        for i,j in starts:
            seen = set()
            for row in range(i, i+3):
                for col in range(j,j+3):
                    curr = board[row][col]
                    if curr in seen:
                        return False
                    elif curr != '.':
                        seen.add(curr)



        return True