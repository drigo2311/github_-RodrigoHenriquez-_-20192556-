import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(num1, num2):
    return num1 + num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    num1 = 1
    result = 0
    while num1 <= 1000:
        if num1 % 2 == 0:
            result += num1
            num1 += 1
        else:
            num1 += 1

    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    x = lambda r, a: 2 * math.pi * r * a
    y = lambda r: 2 * math.pi * r * r
    result = x(radio, altura) + y(radio)
    return round(result, 2)


def areaLateral():
    result = 0
    return result


def areaCirculo():
    result = 0
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def areaTotalCilindro(self, radio, altura):
        x = lambda r, a: 2 * 3.1415926535897932384 * r * a
        y = lambda r: 2 * 3.1415926535897932384 * r * r
        result = x(radio, altura) + y(radio)
        return round(result, 2)


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def __init__(self):
        self.ordenes = []

    def ordenar(self, pizza):
        pizz1 = pizza
        especial = pizz1.especialidad
        depa = pizz1.departamento
        cost = pizz1.costo
        desc = pizz1.descuento
        cantiD = pizz1.cantidadDes

        orden = (especial, depa, cost, desc, cantiD)
        self.ordenes.append(list(orden))

    def costoTotal(self):
        s = 0
        for x in orden:
            s += list(orden)[2]
        return s

    def costoTotalConDescuento(self):
        v = 0
        for x in orden:
            v += list(orden)[2]
            v -= list(orden)[x]
        return v


# Restaurante.ordenar(Pizza("suprema", "san salvador", 4.99, True, 0.99))
class Pizza:
    def __init__(self, especialidad, departamento, costo, descuento, cantidadDes):
        self.especialidad = especialidad
        self.departamento = departamento
        self.costo = costo
        self.descuento = descuento
        self.cantidadDes = cantidadDes


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
