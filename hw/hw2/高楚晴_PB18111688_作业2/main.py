PI = 3.1415926

def sum_of_all(a, b, *args, **optional):
    '''
    return sum of parameters
    parameter could not be less than two
    optional block: defualt is 1, when set to 2,will multi two together
    optional inverse: default is False, when set to True, sum inverse instead  
    '''
    res = 0.0
    args_list = list(args)
    args_list.insert(0,b)
    args_list.insert(0,a)
    if 'inverse' in optional and optional['inverse'] == True:
        for i in range(len(args_list)):
            args_list[i] = 1/args_list[i]
    if 'block' in optional and optional['block'] == 2:
        for i in range(0,len(args_list)-1,2):
            res += args_list[i] * args_list[i+1]
        if not i+2 == len(args_list):
            res += args_list[i+2]
        return res
    return sum(args_list)

class Shape:
    def __init__(self, name = '', area = 0):
        self.area = area
        self.name = name
    def get_area(self):
        return self.area

class Circle(Shape):
    def __init__(self,diameter=2):
        self.diameter = diameter
        self.area = diameter**2*PI/4
    
class Square(Shape):
    def __init__(self,side=1):
        self.side = side
        self.area = side**2

