#!/usr/bin/env python

"""
Faça um Programa que converta metros para centímetros.
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
    metros = get_number("Valor em metros: ")
    print("{} metros = {} centímetros".format(metros, float_or_int(metros*100)))
