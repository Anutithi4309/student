class CSSstudent:
    stream='cse'
    def __init__(self,roll): 
        self.roll=roll
    def setAdress(self,adress):
         self.adress=adress
    def getadress(self):
         return self.adress
add=CSSstudent (101) 
add.setAdress("pune,Maharashtra")
print(add.getadress())
a=CSSstudent(101)
b=CSSstudent(102)
print(a.stream)
print(b.stream)
print(a.roll)
print(CSSstudent.stream)
    