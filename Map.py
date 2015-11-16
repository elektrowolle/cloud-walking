from PIL import Image
__author__ = 'benjaminskirlo1'

class Map:
    image = Image.open("map.png")
    meta  = {};

    def getNode(self, _coordinates):
        if _coordinates in self.meta:
            return self.meta[_coordinates]

        self.meta[_coordinates] = sum(self.image.getpixel(_coordinates))
        
        return self.getNode(_coordinates)

if __name__ == "___main___":
    print("hallo")
