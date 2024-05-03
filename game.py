import helper
from board import Board
from car import Car


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print(self.board)
        playerinput = input('enter the car name and the direction')
        if playerinput == '!':
            return False
        else:
            inputs = playerinput.split(',')
            if len(inputs) == 2:
                if self.board.move_car(inputs[0],inputs[1]) == False:
                    print('unvalid inputs')
                else:
                    print('car moved')
            else:print('invalid input')
            return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        wanttoplay = self.__single_turn()
        while wanttoplay:
            if self.board.cell_content(self.board.target_location()) is None:
                wanttoplay = self.__single_turn()
            else:
                print('you win')
                break


if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    names = ['Y', 'B', 'O', 'G', 'W', 'R']
    c = helper.load_json('car_config.json')
    board = Board()
    for car in c:
        if car in names:
            if c[car][0] == 2 or c[car][0] == 3 or c[car][0] == 4:
                if c[car][2] == 0 or c[car][2] == 1:
                    toadd = Car(car,c[car][0],tuple(c[car][1]),c[car][2])
                    board.add_car(toadd)
    game = Game(board)
    game.play()




