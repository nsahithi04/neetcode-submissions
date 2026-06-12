class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        cols=defaultdict(set)
        square=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in square[(i//3,j//3)]
                    or board[i][j] in row[i]
                    or board[i][j] in cols[j]):
                    return False
                else:
                    row[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    square[(i//3,j//3)].add(board[i][j])

        return True
                    


   

                