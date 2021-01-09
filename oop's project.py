import matplotlib.pyplot as plt

class Shape():
    #constertor 
    def __init__(self,length,width,color):
        self.length = length
        self.width = width
        self.color = color

    #find area 
    def Rectangle_area(self):
        return self.length * self.width

    #specially for making squares
    @classmethod
    def squre(cls,length,color):
        return cls(length,length,color)

    #for vizualizing results
    def draw(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.length ,fc=self.color))
        plt.axis('scaled')
        plt.show()

#applying static method
s = Shape.squre(5,'red')
print(s.Rectangle_area())
s.draw() 


#making rectangle
""" r = Shape(3,5,'blue')
print(r.Rectangle_area())
r.draw() """