

class Vector:
    x = 0
	y = 0
	z = 0
	def __init__(self, x, y, z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

    def __dot__(self, v2):        # dot product
	    return (self.x*v2.x +  self.y*v2.y + self.z*v2.z)

    def __cross__(self, v2):      #cross product
	    return Vector(self.y*v2.z - self.z*v2.y, 
                        self.z*v2.x - self.x*v2.z, 
			            self.z*v2.y - self.y*v2.x)
    def __operatorplus__(self, v2):
        return Vector(self.x + v2.x, 
                        self.y + v2.y, 
			            self.z + v2.z)
    
    def __operatorpluss__(self, v2):
        self.x += v2.x
        self.y += v2.y
        self.z = v2.z
        

    def __operatorminus__(self, v2):
        return Vector(self.x - v2.x, 
                        self.y - v2.y, 
			            self.z - v2.z)

    def __operatorpluss__(self, v2):
        self.x -= v2.x
        self.y -= v2.y
        self.z -= v2.z


    def __scalarmult__(self, c):
        return Vector( c*self.x, c*self.y,  c*self.z)




