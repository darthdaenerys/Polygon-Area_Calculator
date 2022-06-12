class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,x):
        self.width=x
    
    def set_height(self,x):
        self.height=x

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5
    
    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        else:
            ans=''
            for i in range(self.height):
                for j in range(self.width):
                    ans+='*'
                ans+='\n'
            return ans
    
    def get_amount_inside(self,shape):
        return (self.width//shape.width)*(self.height//shape.height)

class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self,x):
        self.width=x
        self.height=x
    