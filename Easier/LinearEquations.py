#  File: LinearEquations.py
#  Description: The purpose of this program is to utilize the class LinearEquation to create, print, and perform operations on linear equations such as addition, subtraction. composition, and evaluation.
#  Student's Name: Giovanni Medrano


############################################################################

class LinearEquation():
    
#  Creates the constructor for each object.
    def __init__(self, m, b):
        self.m = m
        self.b = b
        
#  returns a string of form "mx + b" whilst keeping track of negatives symbols.

    def showEq(self):
        eq = ""
        if (self.m != 0):
            if (self.m > 0):
                eq = str(self.m) + "x"
            else:
                eq = "- " + str(-1 * self.m) + "x"
                
        if self.b != 0:            
            if self.b > 0:
                if len(eq) > 0:
                    eq = eq + " + " + str(self.b)
                else:
                    eq = str(self.b)
            else:
                if len(eq) > 0:
                 #   self.b = (self.b * -1)
                    eq = eq + " - " + str(-1 * self.b)
                else:
                    eq = "- " + str(-1 * self.b)

        return eq
    
#  These are the methods that carry out each of the simple operations.                    

    def add(self, eq2):
        return LinearEquation(self.m + eq2.m, self.b + eq2.b)
    
    def sub(self, eq2):
        return LinearEquation(self.m - eq2.m, self.b - eq2.b)
    
    def compose(self, eq2):
        return LinearEquation(self.m * eq2.m, self.m * eq2.b + self.b)
    
    def evaluate(self, val):
        return(self.m * val +self.b)
    

def main():
    
   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

main()
