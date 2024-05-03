class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.cars_list = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.
        board = ''
        for i in range(7):
            for j in range(7):
                if self.cell_content((i,j)) is None:
                    board = board + '_'
                else:
                    board = board + self.cell_content((i,j))
            if i == 3:
                board = board + 'E' + '\n'
            else:
                board = board +'*' + '\n'
        return board



    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        celllist = []
        for i in range(7):
            for j in range(7):
                celllist.append((i, j))
        celllist.append((3, 7))
        return celllist

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        possiblemoves = []
        for car in self.cars_list:
            if car.orientation == 0:
                coordinates = car.movement_requirements('u')
                for c in coordinates:
                    if c in self.cell_list() and self.cell_content(c) is None:
                        possiblemoves.append((car.get_name(), 'u', "your car can move to the up"))
                coordinates = car.movement_requirements('d')
                for c in coordinates:
                    if c in self.cell_list() and self.cell_content(c) is None:
                        possiblemoves.append((car.get_name(), 'd', "your car can move to the down"))
            if car.orientation == 1:
                coordinates = car.movement_requirements('l')
                for c in coordinates:
                    if c in self.cell_list() and self.cell_content(c) is None:
                        possiblemoves.append((car.get_name(), 'l', "your car can move to the left"))
                coordinates = car.movement_requirements('r')
                for c in coordinates:
                    if c in self.cell_list() and self.cell_content(c) is None:
                        possiblemoves.append((car.get_name(), 'r', "your car can move to the right"))
        return possiblemoves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        for car in self.cars_list:
            coordinates = car.car_coordinates()
            if coordinate in coordinates:
                return car.name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        for i in self.cars_list :
            if car.name == i.name :
                return False
        carcoordinates = car.car_coordinates()
        for j in carcoordinates :
            if j not in self.cell_list():
                return False
            if self.cell_content(j) is not None:
                return False
        self.cars_list.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for car,current_move,_ in self.possible_moves():
            if name == car and movekey == current_move:
                for i in self.cars_list:
                    if i.get_name() == name:
                        i.move(movekey)
                        return True
        return False


