class Car:
    def __init__(self, doors, tires, seats, color, acelerator, breaker, reverse):     # our attributes are defined in a special function __init__, and we need to use self to refer our attributes
        self.doors = doors
        self.tires = tires
        self.seats = seats
        self.color = color
        self.acelerator = acelerator
        self.breaker = breaker
        self.reverse = reverse
        
    def speed_up(self):    # we always will need to use self to refer
        if self.acelerator == 'acelerating':    #the user will declare a value for acceleration, as well as for the other attributes 
            print('the car is going forward')
    
    def brake(self):
        if self.breaker == 'breaking':
            print('the car is stopping')

    def reversing(self):
        if self.reverse == 'reversing':
            print('the car is reversing')