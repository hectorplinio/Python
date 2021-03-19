class Calculadora:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def suma(self):
        print("El resultado de la suma es " + str(self.num1 + self.num2))
    
    def resta(self):
        print("El resultado de la resta es " + str(self.num1 - self.num2))
    
    def multiplicacion(self):
        print("El resultado de la multiplicacion es " + str(self.num1 * self.num2))
    
    def division(self):
        print("El resultado de la division es " + str(self.num1 / self.num2))
    


n=Calculadora(5,6)
n.suma()
n.resta()
n.multiplicacion()
n.division()