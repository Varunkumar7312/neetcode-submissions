class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen=[]

            for val in row:
                if val==".":
                   continue

                if val in seen:
                    return False

                seen.append(val)

        for col in range(9):
            seen=[]

            for row in range(9):
                val = board[row][col]

                if val ==".":
                    continue
                if val in seen:
                        
                    return False

                seen.append(val)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):

                seen=[]

                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        val=board[r][c]

                        if val==".":
                            continue


                        if val in seen:
                            return False

                        seen.append(val)
            return True                       

                                    