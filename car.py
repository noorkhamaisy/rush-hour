class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        l = list()
        if self.orientation == 1:
            for i in range(self.length):
                l.append((self.location[0], self.location[1] + i))
        if self.orientation == 0:
            for j in range(self.length):
                l.append((self.location[0] + j, self.location[1]))
        return l

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        #For this car type, keys are from 'udrl'
        #The keys for vertical cars are 'u' and 'd'.
        #The keys for horizontal cars are 'l' and 'r'.
        #You may choose appropriate strings.
        # implement your code and erase the "pass"
        #The dictionary returned should look something like this:
        #result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        #A car returning this dictionary supports the commands 'f','d','a'.
        if self.orientation == 1:
            Dict = dict({'r': "your car can move to the right", 'l': "your car can move to the left"})
        if self.orientation == 0:
            Dict = dict({'u': "your car can move to the up", 'd': "your car can move to the down"})
        return Dict

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        l = list()
        if movekey == 'u' and self.orientation == 0:
            l.append((self.location[0] - 1, self.location[1]))
        if movekey == 'd' and self.orientation == 0:
            coordinate = self.car_coordinates()[-1]
            l.append((coordinate[0] + 1, coordinate[1]))
        if movekey == 'l' and self.orientation == 1:
            l.append((self.location[0], self.location[1] - 1))
        if movekey == 'r' and self.orientation == 1:
            coordinate2 = self.car_coordinates()[-1]
            l.append((coordinate2[0], coordinate2[1] + 1))
        return l

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if movekey == 'u' and self.orientation == 0:
            self.location = self.location[0] - 1, self.location[1]
            return True
        if movekey == 'd' and self.orientation == 0:
            self.location = self.location[0] + 1, self.location[1]
            return True
        if movekey == 'l' and self.orientation == 1:
            self.location = self.location[0], self.location[1] - 1
            return True
        if movekey == 'r' and self.orientation == 1:
            self.location = self.location[0], self.location[1] + 1
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.name
