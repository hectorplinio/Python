class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    
    def tipo(self):
        if self.lado1 > self.lado2:
            if self.lado1 > self.lado3:
                print (self.lado1)
            else:
                print (self.lado3)
        elif self.lado2 > self.lado1:
            if self.lado2 > self.lado3:
                print (self.lado2)
            else:
                print (self.lado3)
        elif self.lado3 > self.lado1:
            if self.lado3 > self.lado2:
                print (self.lado3)
            else:
                print (self.lado2)
        elif self.lado1 == self.lado2:
            print (self.lado1 , self.lado2)
        elif self.lado2 == self.lado3:
            print (self.lado2 , self.lado3)
        elif self.lado1 == self.lado3:
            print (self.lado1 , self.lado3)

    def mayor(self):
        if self.lado1 == self.lado2:
            if self.lado3 == self.lado1:
                print("Es un triangulo Equilatero")
            else:
                print("Es un triangulo Isosceles")
        if self.lado3 == self.lado2:
            if self.lado3 == self.lado1:
                print("Es un triangulo Equilatero")
            else:
                print("Es un triangulo Isosceles")
        if self.lado1 != self.lado2:
            if self.lado3 != self.lado1:
                print("Es un triangulo Escaleno")
            else:
                print("Es un triangulo Isosceles")
t1=Triangulo(8,8,6)
t1.tipo()
t1.mayor()