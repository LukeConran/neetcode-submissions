class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            t = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in t:
                        return False
                    else:
                        t.add(board[j][i])        
        
        #0-3, 3-6, 6-9
        for i in range(3, 10, 3):
            for j in range(3, 10, 3):
                u = set()
                for k in range(i-3, i, 1):
                    for l in range(j-3, j, 1):
                        if board[k][l] != ".":
                            if board[k][l] in u:
                                return False
                            else:
                                u.add(board[k][l])
        
        return True


