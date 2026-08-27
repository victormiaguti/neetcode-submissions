class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in board:
            for char in row:
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)
            seen.clear()
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
            seen.clear()
        
        for i in range(1, len(board), 3):
            for j in range(1, len(board), 3):
                for x in range(-1,2):
                    for y in range(-1,2):
                        if board[i+x][j+y] == ".":
                            continue
                        if board[i+x][j+y] in seen:
                            return False
                        seen.add(board[i+x][j+y])
                seen.clear()
        return True
        