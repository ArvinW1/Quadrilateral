from two_d_point import TwoDPoint
import math

class Quadrilateral:

    def __init__(self, *floats):
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])
        if not self.__is_member():
            raise TypeError("A Quadrilateral cannot be formed by the given coordinates.")
        

    def __is_member(self):
        """Returns True if the given coordinates form a valid Quadrilaterial, and False otherwise."""
        vertex = self.__vertices # Return the list of vertices
        if(len(vertex) == 4):
            for i in range(0,4):
                if(vertex[i%4] == vertex[(i+1)%4] or vertex[i%4] == vertex[(i+2)%4]): # Checks if each point is unique
                    return False  # TODO
            return True
        return False

    @property
    def vertices(self):
        return self.__vertices

    def side_lengths(self):
        """Returns a tuple of four floats, each denoting the length of a side of this quadrilateral. The value must be
        ordered clockwise, starting from the top left corner."""
        Side_tuple = []
        for i in range(4,0, -1):
            Side_tuple.append(math.sqrt( ((self.__vertices[(i+1)%4].x - self.__vertices[i%4].x)**2) +  ((self.__vertices[(i+1)%4].y - self.__vertices[i%4].y)**2)))
        return tuple(Side_tuple) # TODO

    def smallest_x(self):
        """Returns the x-coordinate of the vertex with the smallest x-value of the four vertices of this
        quadrilateral."""
        small_x = self.__vertices[0].x
        for i in range(1,4):
            if(small_x > self.__vertices[i].x):
                small_x = self.__vertices[i].x
        return small_x  # TODO
    
    def __eq__(self, other): 
        if(type(self) == type(other)):
            for i in range(0,4):
                if(self.__vertices[i].x != other.vertices[i].x or self.__vertices[i].y != other.vertices[i].y ):
                    return False
            return True
        return False
    
    def __str__(self):
        string = "Quadrilateral with:\n" + "Coordinates: " 
        for i in range(0,4):
            string += str(self.__vertices[i])
            string += " "
        string += "\nSides lengths: ("
        for i in range(0,4):
            string += str(self.side_lengths()[i])
            if(i != 3):
                string += ", "
        string += ")"
        return string