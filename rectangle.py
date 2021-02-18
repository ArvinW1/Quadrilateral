from two_d_point import TwoDPoint
from quadrilateral import Quadrilateral



class Rectangle(Quadrilateral):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __is_member(self):
        """Returns True if the given coordinates form a valid rectangle, and False otherwise."""
        vertex = self.vertices # Return the list of vertices
        for i in range(0,4):
            if(vertex[i%4] == vertex[(i+1)%4] or vertex[i%4] == vertex[(i+2)%4]): # Checks if each point is unique
                return False  # TODO
        lengthOfSides = self.side_lengths()
        return lengthOfSides[0] == lengthOfSides[2] and lengthOfSides[1] == lengthOfSides[3]
            

    def center(self):
        """Returns the center of this rectangle, calculated to be the point of intersection of its diagonals."""
        vertex = self.vertices # Vertices is a property
        diagonalx = (vertex[0].x + vertex[2].x)/2
        diagonaly = (vertex[0].y + vertex[2].y)/2
        return TwoDPoint(diagonalx, diagonaly)  # TODO

    def area(self):
        """Returns the area of this rectangle. The implementation invokes the side_lengths() method from the superclass,
        and computes the product of this rectangle's length and width."""
        # TODO
        lengthOfSides = self.side_lengths()
        return lengthOfSides[0] * lengthOfSides[1] # Gets the length then * width
    
    def __eq__(self, other):
        if(type(self) == type(other)):
            for i in range(0,4):
                if(self.vertices[i].x != other.vertices[i].x or self.vertices[i].y != other.vertices[i].y ):
                    return False
            return True
        return False
    
    def __str__(self):
        string = "Rectangle with:\n" + "Coordinates: "
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

