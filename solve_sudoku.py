def is_valid(board, row, col, num): #3가지 규칙 체크함수
    #해당 숫자가 같은 행에 있는지 확인
    # 1.에 중복된 숫자가 있는지
    if num in board[row]:          
        return False

    # 2.열에 중복된 숫자가 있는지
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # 3. 3x3박스에 중복된 숫자가 있는지!
    start_row, start_col = 3 * (row // 3), 3 * (col// 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def find_empty_location(board):  #빈 값(0)을 찾는 함수
  #비어있는 위치(0)을 찾음
    for i in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
            
    return None

def solve_sudoku(board):
  #빈 위치 찾기
    empty_loc = find_empty_location(board)
    
    if not empty_loc: # not None = True
        return True  #다 풀었다!

    #빈 위치가 있으면,
    row, col = empty_loc
    for num in range(1, 10):

      #3가지 규칙이 맞을 때,
       if is_valid(board, row, col, num):
          board[row][col] = num
          
          #############재귀함수 (recursive)
          if solve_sudoku(board):
            return True
          
          board[row][col] = 0  #무르기! <- 풀 수 없는 스도쿠가 입력을 들어올 수 있기 때문