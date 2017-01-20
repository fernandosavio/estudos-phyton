#!/usr/bin/env python

"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit
C = (5 * (F-32) / 9).

C = 5 * (F-32) / 9
C * 9 = 5 * (F-32)
(C*9)/5 = F - 32
F = C * 9 / 5 + 32
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
    c = get_number("Graus em Celsius: ")
    f = float(c * 9 / 5 + 32)

    print("{}°F".format(float_or_int(round(f, 2))))

