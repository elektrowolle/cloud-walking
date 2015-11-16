from PIL import Image
import operator
__author__ = 'benjaminskirlo1'

def tupleAdd(a,b): return (a[0] + b[0], a[1] + b[1])

class Map:
    image = Image.open("map.png")
    meta  = {};

    def getCosts(self, _coordinates):
        if _coordinates in self.meta:
            return self.meta[_coordinates]

        self.meta[_coordinates] = sum(self.image.getpixel(_coordinates))

        return self.getNode(_coordinates)

    def getNeighbours(self, _coordinate):
        coordinatesList = [];


        for y in range(-1,2):
            for x in range(-1,2):
                coordinate = tupleAdd((x,y), _coordinate)
                if(0 <= x < self.image.width and 0 <= y < self.image.height and self.costs(coordinate) > 0):
                    coordinatesList.append(coordinate)

        return coordinatesList;        

if __name__ == "___main___":
    print("hallo")
