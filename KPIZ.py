class Math:
    def __init__ (self):
        self.arrayA = []
        self.arrayB = []
        self.arrayC = []
        self.arrayD = []
        self.arrayU = []
       
    def setArrayA(self, arrayA):
        self.arrayA = arrayA;
    def setArrayB(self,arrayB):
        self.arrayB = arrayB;
    def setArrayC(self, arrayC):
        self.arrayC = arrayC;
    def setArrayD(self, arrayD):
        self.arrayD = arrayD;
    def setArrayU(self,arrayU):
        self.arrayU = arrayU;
        
    def getArrayA(self):
        return self.arrayA;
    def getArrayB(self):
        return self.arrayB;
    def getArrayC(self):
        return self.arrayC;
    def getArrayD(self):
        return self.arrayD;
    def getArrayU(self):
        return self.arrayU;
    
    def inputArray(self, string):
        string.replace(', ',',')
        array = string.split(',')
        for x in range(len(array)):
            array[x]=int(array[x])
        return array;

class Arifmetic:
    def Filling (self,x):
        self.arrayN = []
        for i in range(len(x)):
            self.arrayN.append(x[i])
            
    def Association(self, x,y):
        self.Filling(x);
        
        for j in range(len(y)):
            if y[j] not in x:
                self.arrayN.append(y[j])

        self.arrayN.sort()
        return self.arrayN
                   
    def Crossing(self, x,y):
        self.arrayN = []
        
        for i in range(len(x)):
            if x[i] in y:
                self.arrayN.append(x[i])

        self.arrayN.sort()
        return self.arrayN
    
    def RelComplement(self, x,y):
        self.Filling(x);
        
        for i in range(len(x)):
            if x[i] in y:
                self.arrayN.remove(x[i])
        return self.arrayN
    
    def SymmDifference(self, x,y):
        self.arrayN = []
        self.array = self.Association(self.RelComplement(x,y),self.RelComplement(y,x))
        return self.arrayN
    
    def Not(self,x,y):
        self.Filling(x)
            
        for i in range(len(y)):
            if y[i] in x:
                self.arrayN.remove(y[i])
        return self.arrayN
    
    def Dictionary(self, string, x):
        keys = { "A":x.getArrayA(),
                 "B":x.getArrayB(),
                 "C":x.getArrayC(),
                 "D":x.getArrayD(),
                 "U":x.getArrayU(),
                 "`A":self.Not(x.getArrayU(),x.getArrayA()),
                 "`B":self.Not(x.getArrayU(),x.getArrayB()),
                 "`C":self.Not(x.getArrayU(),x.getArrayC()),
                 "`D":self.Not(x.getArrayU(),x.getArrayU())
                 }
        Narray = [keys[string[0]], keys[string[2]]]
        return Narray

    def Dia(self, string, y):
        if string[1] == "(ob)":
            return self.Association(y[0],y[1])
        
        if string[1] == "(per)":
            return self.Crossing(y[0],y[1])

        if string[1] == "(Sem)":
            return self.SymmDifference(y[0], y[1])

        if string[1] == "(vd)":
            return self.RelComplement(y[0], y[1])
        

objec = Math();
string = input();
arr = objec.inputArray(string);
objec.setArrayA(arr);
print(objec.getArrayA())

string2 = input();
arr2 = objec.inputArray(string2);
objec.setArrayB(arr2);
print(objec.getArrayB())

string4 = input();
arr4 = objec.inputArray(string4);
objec.setArrayU(arr4);
print(objec.getArrayU())

nobj = Arifmetic();

string_N=["A","(ob)","B"];

#print(nobj.Association(objec.getArrayA(),objec.getArrayB()))
#print(nobj.Crossing(objec.getArrayA(),objec.getArrayB()))
#print(nobj.RelComplement(objec.getArrayA(),objec.getArrayB()))
print(nobj.Dictionary(string_N,objec))
print(nobj.Dia(string_N, nobj.Dictionary(string_N,objec)))
#print(nobj.SymmDifference(objec.getArrayA(),objec.getArrayB()))
#print(nobj.Not(objec.getArrayU(),objec.getArrayA()))

