class convertor :
    def __init__ (self, from_ , to_ , x) :
        self.from_ =from_
        self.to_ =to_
        self.x =x

    def __cm(self) :
        result=0
        if self.to_== 'Centimeter' :
            result=self.x
        elif self.to_=='Meter' :
            result=self.x / 100
        return result
    
    def __m (self) :
        result=0
        if self.to_== 'Centimeter' :
            result=self.x *100
        elif self.to_=='Meter' :
            result=self.x 
        return result
    
    def unit (self):
        if self.from_=='Centimeter' :
          return  self.__cm()
        elif self.from_=='Meter' :
            return self.__m()