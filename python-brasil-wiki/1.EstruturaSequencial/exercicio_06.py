#!/usr/bin/env python

from math import pi as π

"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""


def float_or_int(number):
    return int(number) if number.is_integer() else float(number)


def get_number(input_question):
    numero = None

    while not numero:
        try:
            numero = float(input(input_question))
            return float_or_int(numero)
        except TypeError:
            raise TypeError("O valor informado deve ser um número (separador de casas decimais deve ser ponto)")


if __name__ == "__main__":
    raio = get_number("Informe o raio: ")
    print("A área é de {} u.a.".format(float_or_int(round(π * raio ** 2, 3))))
