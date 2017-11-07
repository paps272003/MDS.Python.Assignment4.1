class Shapes:    
    def __init__(self,n):
        self.n=n
        
        
    def input_sides(self):
        self.sides=[ int(input('Enter sides '+ str(i+1)+' of triangle :')) for i in range(self.n)] 
         
    def getDisplay(self):
        for i in range(self.n):
            print(" Side  "+ str(i+1)+ ' is :',self.sides[i])
    

class triangle(Shapes):
    
    def __init__(self):
       Shapes.__init__(self,3) 
    
    def calc_area(self):
        a,b,c=self.sides       
        s=(a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
        print('the area of triangle is : %0.2f'%area)