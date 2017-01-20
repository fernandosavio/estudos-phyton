#!/usr/bin/env python

"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
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
    lado = get_number("Informe o lado do quadrado: ")
    area = float(lado ** 2)

    print("A área é de {} u.a.".format(float_or_int(round(area, 3))))
    print("O dobro da área é {}".format(float_or_int(round(area * 2, 3))))
