from quadrilateral import Quadrilateral

class ShapeSorter:

    @staticmethod
    def sort(*args): # Original code just *args
        args = list(args)
        lstsize = len(args) # Gets the size of the list 
        for i in range(0, lstsize):
            minindex = i
            for j in range(i+1, lstsize):
                if(args[minindex].smallest_x() > args[j].smallest_x()):
                    minindex = j # Gets the index of the smallest x
            args[i], args[minindex] = args[minindex], args[i]
        return args
# Test out sorter method and ask more about this with TA - If it should be a list of quadraterial or just args