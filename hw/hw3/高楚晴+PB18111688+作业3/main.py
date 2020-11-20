
class Student:
    '''
    编写一个类Student，构造函数接受一个字符串作为参数，
    定义实例属性name，当用户设置属性name的值时，进行合法性校验。
    校验准则：长度为5-10的字符串，仅仅由大小写字母和数字构成。
    若无法通过校验，则不修改name属性。 
    '''
    def __init__(self,name):
        self.name = name
    def __setattr__(self,name,value):
        #print('access to attribute {} is intercepted'.format(name))
        if name == 'name':
            if not isinstance(value,str):
                #print('only string allowed')
                pass
            elif not 5 <= len(value) <= 10 or value.isalnum() is False:
                #print('wrony type')
                pass
            else:
                object.__setattr__(self,name,value)

class MyDict:
    '''
    编写一个类MyDict，构造函数接受一个字典作为参数，实现字典与字典间的加减乘除运算。
    运算规则：两个MyDict实例对象运算结果总是返回一个新的字典，新字典的键为两个字典共有的键，
    每个键对应的值是参与操作的两个字典中该键对应的值进行相应运算的结果。若被除数为0，结果设置为 'NA'. 
    '''
    def __init__(self,mydict):
        self.mydict = mydict
    def __add__(self,other):
        newdict = {}
        for i in self.mydict:
            if i in other.mydict:
                newdict[i] = self.mydict[i] + other.mydict[i]
        return newdict
    def __sub__(self,other):
        newdict = {}
        for i in self.mydict:
            if i in other.mydict:
                newdict[i] = self.mydict[i] - other.mydict[i]
        return newdict
    def __mul__(self,other):
        newdict = {}
        for i in self.mydict:
            if i in other.mydict:
                newdict[i] = self.mydict[i] * other.mydict[i]
        return newdict
    def __floordiv__(self,other):
        newdict = {}
        for i in self.mydict:
            if i in other.mydict:
                if other.mydict[i]:
                    newdict[i] = self.mydict[i] / other.mydict[i]
                else:
                    newdict[i] = 'NA'
        return newdict
    def __truediv__(self,other):
        newdict = {}
        for i in self.mydict:
            if i in other.mydict:
                if other.mydict[i]:
                    newdict[i] = self.mydict[i] / other.mydict[i]
                else:
                    newdict[i] = 'NA'
        return newdict
        
    

class Student2:
    '''
     编写一个类Student2，构造函数Student2( name = 字符串, score = 浮点数)，
     用户只能通过实例对象读取name和score属性，但不能修改和删除这两个属性的值。 
    '''
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name
        
    @property
    def score(self):
        return self.__score
