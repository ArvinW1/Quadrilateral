from rectangle import Rectangle
from quadrilateral import Quadrilateral
import math


class Square(Rectangle):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    # Have to create a is_member method of square
    def __is_member(self):
        """Returns True if the given coordinates form a valid Square, and False otherwise."""
        vertex = self.vertices # Return the list of vertices
        for i in range(0,4):
            if(vertex[i%4] == vertex[(i+1)%4] or vertex[i%4] == vertex[(i+2)%4]): # Checks if each point is unique
                return False  # TODO 
        lengthOfSides = self.side_lengths()
        for i in range(0,4):
            if(lengthOfSides[i%4] != lengthOfSides[(i+1)%4]): # Checks if the lengths are all equal to each other
                return False
        return True

    def snap(self):
        """Snaps the sides of the square such that each corner (x,y) is modified to be a corner (x',y') where x' is the
        integer value closest to x and y' is the integer value closest to y. This, of course, may change the shape to a
        general quadrilateral, hence the return type. The only exception is when the square is positioned in a way where
        this approximation will lead it to vanish into a single point. In that case, a call to snap() will not modify
        this square in any way."""
        vertex = self.vertices # Gets all the vertices of the quadraterial
        lst = [] # the list that is going to hold 
        for i in range(0,4):
            x = vertex[i].x - int(vertex[i].x) # deceimal value of x coordinate
            y = vertex[i].y - int(vertex[i].y) # Gets the decemial value of x
            if(x >= 0.5 or ( x < 0 and x >= -0.5)):
                x = float(math.ceil(vertex[i].x)) 
            else:
                x = float(math.floor(vertex[i].x)) 
            if(y >= 0.5 or ( y < 0 and y >= -0.5)):
                y = float(math.ceil(vertex[i].y))
            else:
                y = float(math.floor(vertex[i].y))
            lst.append(x) #adds the elements into the list
            lst.append(y)
        for i in range(0,8,2):
            if(lst[i%8] == lst[(i+2)%8] and lst[(i+1)%8] == lst[(i+3)%8] or lst[i%8] == lst[(i+4)%8] and lst[(i+1)%8] == lst[(i+5)%8]):
                return self # Checks if there are any points that are missing after being snapped    
        return Quadrilateral(*lst) # Creates the new quadlaterial with the list
        # TODO
    
    def __eq__(self, other):
        if(type(self) == type(other)):
            for i in range(0,4):
                if(self.vertices[i].x != other.vertices[i].x or self.vertices[i].y != other.vertices[i].y ):
                    return False
            return True
        return False
    
    def __str__(self):
        string = "Square with:\n" + "Coordinates: " 
        for i in range(0,4):
            string += str(self.vertices[i])
            string += " "
        string += "\nSides lengths: ("
        for i in range(0,4):
            string += str(self.side_lengths()[i])
            if(i != 3):
                string += ", "
        string += ")"
        return string