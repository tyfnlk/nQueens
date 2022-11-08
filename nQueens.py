"""Terry Leeshanok"""
class Puzzle:
    """ This class creates the puzzle for the n-queens problem."""

    # defining instance variable variables of puzzle
    def __init__(self, n: int):
        # save value of n
        self.n = n
        # create solution count
        self.solutionCount = 0
        # create a list of lists to act as 2d array for board relative to n
        self.board = [[0 for i in range(self.n)] for x in range(self.n)]
        # keep track of how many queens are on the board
        self.queen_count = 0
        # track of moves made on board - (more for debugging)
        self.move_stack = []

    # simplify solve function to not need any variables
    def solve(self):
        self.find_a_safe_place(0)

    # method to check if a position on the board is safe for a queen ( only considers queens on the same row, or above)
    def is_safe(self, row: int, col: int):
        """given a coordinate, checks if there are any other queens in the column,
            diagonally to the left and diagonally right"""
        # check if there is a queen in the current row
        if self.board[row].__contains__(int(1)):
            return False
        # check if there is a queen above current position
        for a in range(0, row + 1):
            if self.board[row - a][col] == 1:
                return False

        # checks if there is a queen in the diagonal plane (up,left)
        for b in range(0, self.n):
            # keep all positions checked diagonally left within board
            if row - b >= 0 and col - b >= 0:

                if self.board[row - b][col - b] == 1:
                    return False

        # check if there is queen in the diagonal plane (up, right)
        for c in range(0, self.n):
            # keep all positions checked diagonally right within board
            if row - c >= 0 and col + c <= self.n - 1:

                if self.board[row - c][col + c] == 1:
                    p
                    return False
        # return true if passes all checks above. position is safe
        return True

    def find_a_safe_place(self, row: int):
        """recursive function to find safe places on board and find all solutions"""
        # basecase for recursive call: if number of queens
        if row == self.n:
            # increase total solution count
            self.solutionCount += 1
            # title board
            print('solution #', self.solutionCount)
            # display board
            self.display_board()
        else:
            # print(self.move_stack)
            # self.display_board()

            # loop to find safe place in row
            for col in range(self.n):

                if self.is_safe(row, col):
                    # if there is a safe place found, place queen
                    self.place_queen(row, col)
                    # recursive call to attempt to find a safe place in next row
                    self.find_a_safe_place(row + 1)
                    # remove queen if call is returned to
                    self.remove_queen(row, col)

    def place_queen(self, row: int, col: int):
        '''takes a (x,y) coordinate of board and places a queen in that position
            updates queen_count, and adds move to move_stack'''
        # place queen in given location
        self.board[row][col] = 1
        # increase queen count
        self.queen_count += 1
        # store queen location in movestack
        self.move_stack.append((row, col))

    def remove_queen(self, row: int, col: int):
        '''takes a (row, col) coordinate of the board and removes the queen in that location,
            updates moves stack and queen count'''
        # check if there is actually a queen in position
        if self.board[row][col] == 1:
            # changes 0 to 1
            self.board[row][col] = 0
            # update queen count
            self.queen_count -= 1
            # update move stack
            self.move_stack.pop()

    def display_board(self,):


        for i in range(self.n):  # for loop to iterate through each row
            print(self.board[i]) # print each row


while True:
    try: # try block to catch value error of user
        n = (input("please enter a value between 1 and 10, (0 to exit)")) #ask user for input

        if 0 < int(n) <=10:  # print results of puzzle if n is between 1 and 10
            p=Puzzle(int(n))
            p.find_a_safe_place(0)
            print('there are', p.solutionCount, 'solutions for', p.n, 'Queens.')
        elif n ==0: # exit if user enter 0
            exit(0)

    except ValueError: # if input wrong, retry
        print('invalid entry, please try again.')  # ask user to retry if input not 0-10