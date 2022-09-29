# OOP Python 3
This repository was created with the objective of storing all the files made in the classroom for the practice of object orientation from Python.
The entire collection will be available, however, most likely most code will not have a defined documentation.
![python](https://user-images.githubusercontent.com/95464654/192111687-31fee261-3d44-4af1-902b-5026c7ca418d.png)

## How does object orientation work?
Object orientation is focused on generating objects within our codes from classes, so when we study this topic present in programming languages, we will come across these terms that make up object orientation, such as classes, objects, methods and attributes, and we will talk about them all one by one.

## Classes
Classes can be compared with a kind of recipe, in which you will have all the descriptions of something, and these descriptions will be inside the classes.
a class is the specification of a type, defining values ​​and behaviors
### Example: car
let's create a class called car, it will tell us everything a car will need and what it does: a car needs wheels, engine, windshield, seats... and what does it do? it goes forward, backward, from point A to point B, correct? so we have our car class with the complete description of what a car does, and this description will be contained through the methods, attributes and objects, which we will talk about next
Example of our car class created in Python:
``` 
class Car:
    #here we will define our attributes

    #here we will define our méthods
```

## Attributes
the attributes will be all the elements that a car has, as we had exemplified: doors, seats, tires... these attributes we define in a similar way to variables, and we will make use of all the necessary attributes within the methods (this is the first part of our description of a car in the car class)
``` 
class Car:
    def __init__(self, doors, tires, seats, color, acelerator, break, reverse):     # our attributes are defined in a special function __init__, and we need to use self to refer our attributes
        self.doors = doors
        self.tires = tires
        self.seats = seats
        self.color = color
        self.acelerator = acelerator
        self.breaker = breaker
        self.reverse = reverse

    #here we will define our méthods
```
## Methods
the methods are the actions of the car, as mentioned before, which is to go forward, to reverse, to go from point A to point b.
To define methods, each method is defined as a function, and we must then call the attributes that may be needed to perform this action.

class Car:
```
    def __init__(self, doors, tires, seats, color, acelerator, break, reverse):     # our attributes are defined in a special function __init__, and we need to use self to refer our attributes
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
```

## Objects
now that we have our methods and attributes describing our car class and what it does, we can move on to the object definition. An object is created inside the windows or linux terminal, it will be as its name says, an object belonging to our class, so in our example, an object of the car class would be a car, we know that there are thousands of cars today, so there are thousands of car class objects today, that's the idea
a car object would be a specific car with specific attributes that we will define inside the terminal, example below:
```
>>> car1.color
'blue'
>>> car1.accelerator
'accelerating'
>>>
>>> car2 = Car(4, 4, 4, 'red', 'none', 'breaking', 'none')
>>> car2.color
'red'
>>> car2.brake()
the car is stopping
>>> car1.brake()
>>> car1.speed_up()
the car is going forward
>>>
```
In the examples above, I created the objects car1 and car2, one is accelerating and the other is not, and I did it inside the terminal, where I defined the values ​​that will be read inside the init function of the class attributes. when I wrote 'car1.color', it returned me the attribute defined by me for the attribute name I chose, in this case 'color'. when I wrote 'car2.breaking()' it gave me back the action of the car, whether it is braking or not. Notice that when I typed car1.brake(), nothing happened, because my car1 isn't braking, interesting, isn't it?

the file with the complete code is called car.py if you want to see it. in other text files, we will have more advanced explanations and definitions, involving get, set and encapsulation, but for now with these 3 concepts we already have a notion of object orientation
