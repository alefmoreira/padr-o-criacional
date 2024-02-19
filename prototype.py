from copy import deepcopy

class Shape:
    def clone(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def clone(self):
        return deepcopy(self)


class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def clone(self):
        return deepcopy(self)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def clone(self):
        return deepcopy(self)



circulo_original = Circle(5, "Azul")
circulo_clonado = circulo_original.clone()
print(circulo_original.radius, circulo_original.color)
print(circulo_clonado.radius, circulo_clonado.color)

retangulo_original = Rectangle(4, 6, "Verde")
retangulo_clonado = retangulo_original.clone()
print(retangulo_original.width, retangulo_original.height, retangulo_original.color)
print(retangulo_clonado.width, retangulo_clonado.height, retangulo_clonado.color)

triangulo_original = Triangle(3, 4, 5, "Vermelho")
triangulo_clonado = triangulo_original.clone()
print(triangulo_original.side1, triangulo_original.side2, triangulo_original.side3, triangulo_original.color)
print(triangulo_clonado.side1, triangulo_clonado.side2, triangulo_clonado.side3, triangulo_clonado.color)
